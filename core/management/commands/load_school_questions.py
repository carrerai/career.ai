from django.core.management.base import BaseCommand
from core.models import SchoolQuestion
import json
import os

class Command(BaseCommand):
    help = 'Load school questions from JSON file into database'

    def handle(self, *args, **options):
        # Clear existing questions
        SchoolQuestion.objects.all().delete()
        self.stdout.write('Cleared existing school questions')

        # Load questions from JSON file
        json_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'psychometric_questions.json')
        
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
                questions = data['questions']
                
                # Create SchoolQuestion objects
                for question_data in questions:
                    SchoolQuestion.objects.create(
                        id=question_data['id'],
                        text=question_data['text'],
                        trait=question_data['trait'],
                        stream_hint=question_data['stream_hint']
                    )
                
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully loaded {len(questions)} school questions')
                )
                
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'JSON file not found at {json_file_path}')
            )
        except json.JSONDecodeError:
            self.stdout.write(
                self.style.ERROR('Invalid JSON format in the file')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error loading questions: {str(e)}')
            )
