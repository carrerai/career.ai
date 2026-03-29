from django.core.management.base import BaseCommand
from core.models import Question, Option

class Command(BaseCommand):
    help = 'Remove duplicate questions from database'

    def handle(self, *args, **options):
        # Get all question texts
        all_questions = Question.objects.all()
        question_texts = list(all_questions.values_list('text', flat=True))
        
        # Find duplicates
        seen = set()
        duplicates = []
        
        for text in question_texts:
            if text in seen:
                duplicates.append(text)
            else:
                seen.add(text)
        
        # Remove duplicate questions and their options
        removed_count = 0
        for duplicate_text in duplicates:
            questions_to_remove = Question.objects.filter(text=duplicate_text)
            for question in questions_to_remove[1:]:  # Keep first, remove rest
                options = question.options.all()
                for option in options:
                    option.delete()
                question.delete()
                removed_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Removed {removed_count} duplicate questions')
        )
        
        # Show current counts
        aptitude_count = Question.objects.filter(test_type='aptitude').count()
        interest_count = Question.objects.filter(test_type='interest').count()
        personality_count = Question.objects.filter(test_type='personality').count()
        
        self.stdout.write(
            self.style.SUCCESS(f'Current counts - Aptitude: {aptitude_count}, Interest: {interest_count}, Personality: {personality_count}')
        )
