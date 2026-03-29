from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
import uuid
from .models import Question, Option, TestSession, UserResponse, Result
from .career_logic import get_career_recommendations, generate_career_guidance

# Create your views here.

def home(request):
    return render(request, 'core/home.html', {'user': request.user})

@method_decorator(login_required, name='dispatch')
class StartTestView(View):
    def get(self, request):
        # Create new test session linked to user
        session = TestSession.objects.create(
            user=request.user,
            session_id=str(uuid.uuid4())
        )
        return redirect('test_step', session_id=session.session_id, step=1)

@method_decorator(login_required, name='dispatch')
class TestStepView(View):
    def get(self, request, session_id, step):
        session = get_object_or_404(TestSession, session_id=session_id)
        
        def get_balanced_questions(test_type, traits, per_trait=4):
            """Get equal distribution of questions per trait"""
            questions = []
            for trait in traits:
                qs = Question.objects.filter(test_type=test_type, trait=trait).order_by('?')[:per_trait]
                questions.extend(qs)
            return questions
        
        if step == 1:  # Aptitude
            questions = get_balanced_questions('aptitude', ['logical', 'quantitative', 'analytical'], 7)
            template_name = 'core/test_aptitude.html'
        elif step == 2:  # Interest
            questions = get_balanced_questions('interest', ['R', 'I', 'A', 'S', 'E', 'C'], 3)
            template_name = 'core/test_interest.html'
        elif step == 3:  # Personality
            questions = get_balanced_questions('personality', ['O', 'C', 'E', 'A', 'N'], 4)
            template_name = 'core/test_personality.html'
        else:
            return redirect('test_result', session_id=session_id)
        
        # Load options for each question
        for question in questions:
            question.options_list = question.options.all()
        
        context = {
            'session': session,
            'questions': questions,
            'current_step': step,
            'total_steps': 3
        }
        
        return render(request, template_name, context)
    
    def post(self, request, session_id, step):
        session = get_object_or_404(TestSession, session_id=session_id)
        
        # Save responses
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                question = get_object_or_404(Question, id=question_id)
                
                if question.is_mcq:
                    # Get selected option
                    option_id = value
                    option = get_object_or_404(Option, id=option_id)
                    UserResponse.objects.create(
                        session=session,
                        question=question,
                        selected_option=option,
                        answer_value=option.score
                    )
                else:
                    # Scale question
                    answer_value = int(value)
                    UserResponse.objects.create(
                        session=session,
                        question=question,
                        answer_value=answer_value
                    )
        
        # Move to next step
        next_step = step + 1
        if next_step <= 3:
            return redirect('test_step', session_id=session_id, step=next_step)
        else:
            return redirect('test_result', session_id=session_id)

@method_decorator(login_required, name='dispatch')
class TestResultView(View):
    def get(self, request, session_id):
        session = get_object_or_404(TestSession, session_id=session_id)
        
        # Check if result already exists
        if hasattr(session, 'result'):
            result = session.result
        else:
            # Calculate scores and generate result
            result = self.calculate_result(session)
        
        context = {
            'session': session,
            'result': result
        }
        
        return render(request, 'core/test_result.html', context)
    
    def calculate_result(self, session):
        responses = UserResponse.objects.filter(session=session)
        
        def normalize_score(responses, max_per_question=5):
            """Convert raw scores to percentage (0-100)"""
            total = sum(r.answer_value if r.answer_value is not None else r.selected_option.score for r in responses)
            max_score = len(responses) * max_per_question
            return (total / max_score) * 100 if max_score > 0 else 0
        
        # Calculate aptitude scores (normalized to percentage)
        aptitude_scores = {}
        for trait in ['logical', 'quantitative', 'analytical']:
            trait_responses = responses.filter(question__test_type='aptitude', question__trait=trait)
            aptitude_scores[trait] = normalize_score(trait_responses)
        
        # Calculate interest scores (RIASEC) - normalized to percentage
        interest_scores = {}
        for trait in ['R', 'I', 'A', 'S', 'E', 'C']:
            trait_responses = responses.filter(question__test_type='interest', question__trait=trait)
            interest_scores[trait] = normalize_score(trait_responses)
        
        # Calculate personality scores (Big Five) - normalized to percentage
        personality_scores = {}
        for trait in ['O', 'C', 'E', 'A', 'N']:
            trait_responses = responses.filter(question__test_type='personality', question__trait=trait)
            personality_scores[trait] = normalize_score(trait_responses)
        
        # Get career recommendations 
        recommendations = get_career_recommendations(
            aptitude_scores, interest_scores, personality_scores
        )
        
        # Generate AI guidance
        ai_guidance = generate_career_guidance(recommendations)
        
        # Create result
        result = Result.objects.create(
            session=session,
            aptitude_scores=aptitude_scores,
            interest_scores=interest_scores,
            personality_scores=personality_scores,
            top_domain=recommendations['top_domain'],
            recommended_degrees=recommendations['recommended_degrees'],
            ai_guidance=ai_guidance
        )
        
        # Mark session as completed
        session.is_completed = True
        session.save()
        
        return result

@method_decorator(csrf_exempt, name='dispatch')
class SaveResponseView(View):
    def post(self, request):
        data = json.loads(request.body)
        session_id = data.get('session_id')
        question_id = data.get('question_id')
        answer_value = data.get('answer_value')
        option_id = data.get('option_id')
        
        session = get_object_or_404(TestSession, session_id=session_id)
        question = get_object_or_404(Question, id=question_id)
        
        # Delete existing response for this question
        UserResponse.objects.filter(session=session, question=question).delete()
        
        # Create new response
        if option_id:
            option = get_object_or_404(Option, id=option_id)
            response = UserResponse.objects.create(
                session=session,
                question=question,
                selected_option=option,
                answer_value=option.score
            )
        else:
            response = UserResponse.objects.create(
                session=session,
                question=question,
                answer_value=answer_value
            )
        
        return JsonResponse({'status': 'success', 'response_id': response.id})

# Authentication Views
class LoginSignupView(View):
    def get(self, request):
        return render(request, 'core/auth.html')

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        # Validation
        if not all([full_name, email, password, confirm_password]):
            return JsonResponse({'status': 'error', 'message': 'All fields are required'})
        
        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})
        
        if len(password) < 6:
            return JsonResponse({'status': 'error', 'message': 'Password must be at least 6 characters'})
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists'})
        
        # Create user
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=full_name.split()[0] if full_name else '',
                last_name=' '.join(full_name.split()[1:]) if len(full_name.split()) > 1 else ''
            )
            
            # Auto login
            login(request, user)
            
            return JsonResponse({
                'status': 'success', 
                'message': 'Account created successfully',
                'user': {
                    'full_name': full_name,
                    'email': email
                }
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return JsonResponse({'status': 'error', 'message': 'Email and password are required'})
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            full_name = f"{user.first_name} {user.last_name}".strip()
            if not full_name:
                full_name = user.username
            
            return JsonResponse({
                'status': 'success', 
                'message': 'Login successful',
                'user': {
                    'full_name': full_name,
                    'email': user.email
                }
            })
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid email or password'})

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'status': 'success', 'message': 'Logged out successfully'})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user = request.user
        
        # Get user's test sessions and results
        sessions = TestSession.objects.filter(user=user).order_by('-created_at')
        results = []
        
        for session in sessions:
            if hasattr(session, 'result'):
                results.append({
                    'session_id': session.session_id,
                    'created_at': session.created_at,
                    'completed_at': session.updated_at,
                    'top_domain': session.result.top_domain,
                    'recommended_degrees': session.result.recommended_degrees,
                    'aptitude_scores': session.result.aptitude_scores,
                    'interest_scores': session.result.interest_scores,
                    'personality_scores': session.result.personality_scores,
                    'ai_guidance': session.result.ai_guidance
                })
        
        context = {
            'user': user,
            'results': results,
            'total_tests': len(results)
        }
        
        return render(request, 'core/profile.html', context)
    
    def post(self, request):
        data = json.loads(request.body)
        user = request.user
        
        # Update user info
        full_name = data.get('full_name')
        email = data.get('email')
        
        if full_name:
            name_parts = full_name.split()
            user.first_name = name_parts[0]
            user.last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
        
        if email and email != user.email:
            if User.objects.filter(email=email).exclude(id=user.id).exists():
                return JsonResponse({'status': 'error', 'message': 'Email already exists'})
            user.username = email
            user.email = email
        
        user.save()
        
        return JsonResponse({
            'status': 'success', 
            'message': 'Profile updated successfully',
            'user': {
                'full_name': f"{user.first_name} {user.last_name}".strip() or user.username,
                'email': user.email
            }
        })
