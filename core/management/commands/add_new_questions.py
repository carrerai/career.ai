from django.core.management.base import BaseCommand
from core.models import Question, Option

class Command(BaseCommand):
    help = 'Add 100 new psychometric questions different from existing ones'

    def handle(self, *args, **options):
        # Get existing question texts to avoid duplicates
        existing_texts = set(Question.objects.values_list('text', flat=True))
        
        # New Aptitude Questions (30)
        new_aptitude_questions = [
            # Logical (10)
            {
                'text': 'Find the missing number: 3, 9, 27, ?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('81', 5),
                    ('54', 3),
                    ('36', 2),
                    ('45', 1)
                ]
            },
            {
                'text': 'Find the odd one out: Lion, Tiger, Cow, Leopard',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Cow', 5),
                    ('Lion', 2),
                    ('Tiger', 2),
                    ('Leopard', 2)
                ]
            },
            {
                'text': 'If all students are learners and some learners are teachers, which conclusion is valid?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Some students might be teachers', 5),
                    ('All students are teachers', 1),
                    ('No students are teachers', 1),
                    ('All teachers are students', 1)
                ]
            },
            {
                'text': 'If CAT is coded as DBU, how is DOG coded?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('EPH', 5),
                    ('FQI', 3),
                    ('DPI', 2),
                    ('EOH', 1)
                ]
            },
            {
                'text': 'Complete the series: AB, DE, GH, ?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('JK', 5),
                    ('IJ', 3),
                    ('KL', 2),
                    ('HI', 1)
                ]
            },
            {
                'text': 'A person facing north turns right twice, then left once. Which direction are they facing?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('West', 5),
                    ('North', 2),
                    ('East', 2),
                    ('South', 2)
                ]
            },
            {
                'text': 'If all books are pages and some pages have words, which statement must be true?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Some books might have words', 5),
                    ('All books have words', 1),
                    ('No books have words', 1),
                    ('All words are in books', 1)
                ]
            },
            {
                'text': 'Pointing to a woman, a man says "Her mother is my mother\'s only daughter". How is the woman related to the man?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Daughter', 5),
                    ('Sister', 3),
                    ('Wife', 2),
                    ('Mother', 1)
                ]
            },
            {
                'text': 'Find the next number: 2, 6, 12, 20, 30, ?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('42', 5),
                    ('40', 3),
                    ('36', 2),
                    ('45', 1)
                ]
            },
            {
                'text': 'If January is to July as Monday is to:',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Sunday', 5),
                    ('Tuesday', 2),
                    ('Wednesday', 2),
                    ('Saturday', 2)
                ]
            },
            
            # Quantitative (10)
            {
                'text': 'What is 15% of 240?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('36', 5),
                    ('32', 3),
                    ('40', 2),
                    ('30', 1)
                ]
            },
            {
                'text': 'A shopkeeper sells an item at 20% profit. If the cost price is $200, what is the selling price?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('$240', 5),
                    ('$220', 3),
                    ('$260', 2),
                    ('$180', 1)
                ]
            },
            {
                'text': 'If the ratio of boys to girls is 3:5 and there are 40 girls, how many boys are there?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('24', 5),
                    ('20', 3),
                    ('30', 2),
                    ('35', 1)
                ]
            },
            {
                'text': 'What is the average of 12, 18, 24, 30, 36?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('24', 5),
                    ('20', 3),
                    ('28', 2),
                    ('30', 1)
                ]
            },
            {
                'text': 'A car travels 180 km in 3 hours. What is its speed?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('60 km/h', 5),
                    ('50 km/h', 3),
                    ('70 km/h', 2),
                    ('40 km/h', 1)
                ]
            },
            {
                'text': 'If 5 workers can complete a job in 12 days, how many days will 8 workers take?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('7.5 days', 5),
                    ('8 days', 3),
                    ('10 days', 2),
                    ('6 days', 1)
                ]
            },
            {
                'text': 'An item with marked price $500 is sold at 10% discount. What is the selling price?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('$450', 5),
                    ('$400', 3),
                    ('$475', 2),
                    ('$425', 1)
                ]
            },
            {
                'text': 'What is the compound interest on $1000 at 5% for 2 years?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('$102.50', 5),
                    ('$100', 3),
                    ('$105', 2),
                    ('$110.25', 1)
                ]
            },
            {
                'text': 'Simplify: 25 + 15 × 4 - 10',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('75', 5),
                    ('80', 3),
                    ('70', 2),
                    ('85', 1)
                ]
            },
            {
                'text': 'What is 20% of 25% of 200?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('10', 5),
                    ('8', 3),
                    ('12', 2),
                    ('15', 1)
                ]
            },
            
            # Analytical (10)
            {
                'text': 'Six people are sitting in a row. A is to the right of B, C is to the left of D, E is between A and F. Who is in the middle?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('A', 5),
                    ('B', 2),
                    ('C', 2),
                    ('D', 2)
                ]
            },
            {
                'text': 'In a certain code, PROBLEM is written as OQNCDKL. How is SOLUTION written?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('RTMJUHPM', 5),
                    ('RTNKVJPM', 3),
                    ('RTMJVKPM', 2),
                    ('RTNLVJPM', 1)
                ]
            },
            {
                'text': 'A company has departments A, B, C, D, E. Department A works with B and C, B works with D, C works with E. Which department works with the most others?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('A', 5),
                    ('B', 3),
                    ('C', 2),
                    ('D', 1)
                ]
            },
            {
                'text': 'If all roses are flowers and some flowers bloom in spring, which statement is valid?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('Some roses might bloom in spring', 5),
                    ('All roses bloom in spring', 1),
                    ('No roses bloom in spring', 1),
                    ('All spring flowers are roses', 1)
                ]
            },
            {
                'text': 'Five friends have different heights. John is taller than Mike but shorter than Sarah. Emma is taller than John. Who is the tallest?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('Sarah', 5),
                    ('Emma', 3),
                    ('John', 2),
                    ('Mike', 1)
                ]
            },
            {
                'text': 'In a group of 50 people, 30 speak English, 25 speak Hindi, and 10 speak both. How many speak only English?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('20', 5),
                    ('15', 3),
                    ('25', 2),
                    ('30', 1)
                ]
            },
            {
                'text': 'Complete the pattern: 1, 4, 9, 16, 25, ?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('36', 5),
                    ('30', 3),
                    ('49', 2),
                    ('32', 1)
                ]
            },
            {
                'text': 'A statement is followed by assumptions. Which assumption is implicit?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('Both assumptions are implicit', 5),
                    ('Only assumption I is implicit', 3),
                    ('Only assumption II is implicit', 2),
                    ('Neither assumption is implicit', 1)
                ]
            },
            {
                'text': 'If RED is coded as 5, BLUE as 4, what is GREEN coded as?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('5', 5),
                    ('4', 3),
                    ('6', 2),
                    ('3', 1)
                ]
            },
            {
                'text': 'A company has 4 departments with 15, 20, 25, 30 employees respectively. What is the average employees per department?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('22.5', 5),
                    ('20', 3),
                    ('25', 2),
                    ('18', 1)
                ]
            }
        ]

        # New Interest Questions (35)
        new_interest_questions = [
            # Realistic (R) - 6 questions
            {
                'text': 'I enjoy organizing events',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I like building apps',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I enjoy working with machines',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I like hands-on activities',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I enjoy outdoor sports',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I like practical problem solving',
                'trait': 'R',
                'is_mcq': False
            },
            
            # Investigative (I) - 6 questions
            {
                'text': 'I enjoy public speaking',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I like solving math problems',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I enjoy data analysis',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I like experiments',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I enjoy research',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I like logical puzzles',
                'trait': 'I',
                'is_mcq': False
            },
            
            # Artistic (A) - 6 questions
            {
                'text': 'I like designing posters',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I enjoy creative storytelling',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I like art creation',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I like design tools',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I enjoy innovation',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I like creativity',
                'trait': 'A',
                'is_mcq': False
            },
            
            # Social (S) - 6 questions
            {
                'text': 'I enjoy helping children',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I enjoy teaching concepts',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I enjoy social work',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I enjoy group discussions',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I enjoy mentoring',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I enjoy social interaction',
                'trait': 'S',
                'is_mcq': False
            },
            
            # Enterprising (E) - 6 questions
            {
                'text': 'I like managing teams',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I prefer routine tasks',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like business planning',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like leading projects',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like competition',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like strategy',
                'trait': 'E',
                'is_mcq': False
            },
            
            # Conventional (C) - 5 questions
            {
                'text': 'I like accounting',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I like structured environments',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I like organizing files',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I like documentation',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I like routine work',
                'trait': 'C',
                'is_mcq': False
            }
        ]

        # New Personality Questions (35)
        new_personality_questions = [
            # Openness (O) - 7 questions
            {
                'text': 'I adapt quickly',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I like new experiences',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I trust my instincts',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I am curious',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I explore ideas',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I like innovation',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I enjoy challenges',
                'trait': 'O',
                'is_mcq': False
            },
            
            # Conscientiousness (C) - 7 questions
            {
                'text': 'I stay calm in stress',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I plan everything',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I am detail-oriented',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I stay disciplined',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I stay organized',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I follow routines',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I like structure',
                'trait': 'C',
                'is_mcq': False
            },
            
            # Extraversion (E) - 7 questions
            {
                'text': 'I enjoy leadership',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I take initiative',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I speak confidently',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like risks',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I enjoy socializing',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I enjoy conversations',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I prefer teamwork',
                'trait': 'E',
                'is_mcq': False
            },
            
            # Agreeableness (A) - 7 questions
            {
                'text': 'I cooperate easily',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I overthink things',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I support others',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I get anxious',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I am empathetic',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I stay positive',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I solve conflicts',
                'trait': 'A',
                'is_mcq': False
            },
            
            # Neuroticism (N) - 7 questions
            {
                'text': 'I focus deeply',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I adapt fast',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I handle pressure',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I take feedback well',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I stay motivated',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I enjoy independence',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I stay balanced',
                'trait': 'N',
                'is_mcq': False
            }
        ]

        # Add new questions (only if not already in database)
        added_count = 0
        
        # Add Aptitude Questions
        for q_data in new_aptitude_questions:
            if q_data['text'] not in existing_texts:
                question = Question.objects.create(
                    text=q_data['text'],
                    test_type='aptitude',
                    trait=q_data['trait'],
                    is_mcq=q_data['is_mcq']
                )
                
                if q_data['is_mcq']:
                    for option_text, score in q_data['options']:
                        Option.objects.create(
                            question=question,
                            text=option_text,
                            score=score
                        )
                added_count += 1
        
        # Add Interest Questions
        for q_data in new_interest_questions:
            if q_data['text'] not in existing_texts:
                question = Question.objects.create(
                    text=q_data['text'],
                    test_type='interest',
                    trait=q_data['trait'],
                    is_mcq=False
                )
                
                # Create scale options (1-5) for interest questions
                for i in range(1, 6):
                    Option.objects.create(
                        question=question,
                        text=str(i),
                        score=i
                    )
                added_count += 1
        
        # Add Personality Questions
        for q_data in new_personality_questions:
            if q_data['text'] not in existing_texts:
                question = Question.objects.create(
                    text=q_data['text'],
                    test_type='personality',
                    trait=q_data['trait'],
                    is_mcq=False
                )
                
                # Create scale options (1-5) for personality questions
                scale_labels = ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree']
                for i, label in enumerate(scale_labels, 1):
                    Option.objects.create(
                        question=question,
                        text=label,
                        score=i
                    )
                added_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {added_count} new questions')
        )
