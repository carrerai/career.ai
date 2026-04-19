from django.db import models
from django.contrib.auth.models import User
import uuid

class Question(models.Model):
    TEST_TYPES = [
        ('aptitude', 'Aptitude'),
        ('interest', 'Interest'),
        ('personality', 'Personality'),
    ]
    
    APTITUDE_TRAITS = [
        ('logical', 'Logical Reasoning'),
        ('quantitative', 'Quantitative Ability'),
        ('analytical', 'Analytical Thinking'),
    ]
    
    INTEREST_TRAITS = [
        ('R', 'Realistic'),
        ('I', 'Investigative'),
        ('A', 'Artistic'),
        ('S', 'Social'),
        ('E', 'Enterprising'),
        ('C', 'Conventional'),
    ]
    
    PERSONALITY_TRAITS = [
        ('O', 'Openness'),
        ('C', 'Conscientiousness'),
        ('E', 'Extraversion'),
        ('A', 'Agreeableness'),
        ('N', 'Neuroticism'),
    ]
    
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    test_type = models.CharField(max_length=20, choices=TEST_TYPES, default='aptitude')
    trait = models.CharField(max_length=20, default='logical')  # Specific trait within test type
    is_mcq = models.BooleanField(default=False)  # True for aptitude, False for scale questions
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Question {self.id} - {self.test_type}:{self.trait}"

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    score = models.IntegerField()  # Score contribution (0-5)
    
    def __str__(self):
        return f"Option for {self.question.id}: {self.text}"

class TestSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    current_step = models.IntegerField(default=1)  # 1-4: aptitude, interest, personality, result
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Session {self.session_id} - Step {self.current_step}"

class UserResponse(models.Model):
    session = models.ForeignKey(TestSession, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.SET_NULL)
    answer_value = models.IntegerField(null=True, blank=True)  # for scale questions (1-5)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Response for {self.session.session_id} - Question {self.question.id}"

class SchoolResult(models.Model):
    session = models.OneToOneField(TestSession, on_delete=models.CASCADE, related_name='school_result')
    trait_scores = models.JSONField(default=dict)
    mcq_score = models.IntegerField(default=0)  # Score out of 100
    mcq_percentage = models.FloatField(default=0.0)  # Percentage score
    recommended_stream = models.CharField(max_length=50)
    ai_guidance = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"School Result for {self.session.session_id} - {self.recommended_stream} ({self.mcq_percentage}%)"

class Result(models.Model):
    session = models.OneToOneField(TestSession, on_delete=models.CASCADE, related_name='result')
    aptitude_scores = models.JSONField(default=dict)
    interest_scores = models.JSONField(default=dict)
    personality_scores = models.JSONField(default=dict)
    top_domain = models.CharField(max_length=50)
    recommended_degrees = models.JSONField(default=list)
    ai_guidance = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Result for {self.session.session_id} - {self.top_domain}"

class SchoolQuestion(models.Model):
    """Model for school stream MCQ questions"""
    
    STEPS = [
        (1, 'Step 1'),
        (2, 'Step 2'),
        (3, 'Step 3'),
        (4, 'Step 4'),
        (5, 'Step 5'),
    ]
    
    STREAM_HINTS = [
        ('PCM', 'Physics, Chemistry, Mathematics'),
        ('PCB', 'Physics, Chemistry, Biology'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
    ]
    
    id = models.AutoField(primary_key=True)
    step = models.IntegerField(choices=STEPS, null=True, blank=True)
    text = models.TextField()
    option_a = models.CharField(max_length=255, null=True, blank=True)
    option_b = models.CharField(max_length=255, null=True, blank=True)
    option_c = models.CharField(max_length=255, null=True, blank=True)
    option_d = models.CharField(max_length=255, null=True, blank=True)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], null=True, blank=True)
    stream_hint = models.CharField(max_length=20, choices=STREAM_HINTS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"School Question {self.id} - Step {self.step} ({self.stream_hint})"

class SchoolUserResponse(models.Model):
    session = models.ForeignKey(TestSession, on_delete=models.CASCADE, related_name='school_responses')
    question = models.ForeignKey(SchoolQuestion, on_delete=models.CASCADE, null=True, blank=True)
    selected_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"School Response for {self.session.session_id} - Question {self.question.id}"

