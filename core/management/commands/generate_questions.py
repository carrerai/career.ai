from django.core.management.base import BaseCommand
import google.generativeai as genai
import json
from core.models import Question

class Command(BaseCommand):
    help = 'Generate psychometric test questions using Gemini API'

    def handle(self, *args, **options):
        # Configure Gemini API
        genai.configure(api_key="AIzaSyDTFcU2r990Hx388iADi3DIYbqPOiB2OjY")
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = """You are an expert psychometric test designer.

Generate 50 high-quality psychometric questions for students who have just completed 12th grade, to help determine their most suitable undergraduate field.

IMPORTANT RULES:

1. Each question must measure exactly ONE trait from the following:

   * analytical
   * social
   * creative
   * practical
   * investigative

2. Distribute questions evenly:

   * 10 questions per trait

3. Each question must:

   * Be clear, realistic, and situation-based
   * Avoid generic or obvious statements
   * Be understandable by students aged 16–19

4. Each question must follow a 5-point Likert scale:

   * Strongly Agree (score: +2)
   * Agree (score: +1)
   * Neutral (score: 0)
   * Disagree (score: -1)
   * Strongly Disagree (score: -2)

5. DO NOT include options text in every question. Only define scoring system once globally.

6. Output MUST be in strict JSON format:

{
"questions": [
{
"id": 1,
"text": "I enjoy solving complex logical problems or puzzles.",
"trait": "analytical"
}
]
}

7. Do NOT include explanations, comments, or extra text outside JSON.

Make sure questions are diverse, realistic, and not repetitive."""

        try:
            response = model.generate_content(prompt)
            
            # Clean and parse JSON
            response_text = response.text.strip()
            
            # Remove any potential markdown formatting
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            
            data = json.loads(response_text)
            questions = data["questions"]
            
            # Clear existing questions
            Question.objects.all().delete()
            
            # Create new questions
            for q_data in questions:
                Question.objects.create(
                    text=q_data['text'],
                    trait=q_data['trait']
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully generated {len(questions)} questions')
            )
            
            # Display question distribution
            for trait in ['analytical', 'social', 'creative', 'practical', 'investigative']:
                count = Question.objects.filter(trait=trait).count()
                self.stdout.write(f'{trait}: {count} questions')
                
        except json.JSONDecodeError as e:
            self.stdout.write(
                self.style.ERROR(f'Error parsing JSON response: {e}')
            )
            self.stdout.write(f'Raw response: {response.text}')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error generating questions: {e}')
            )
