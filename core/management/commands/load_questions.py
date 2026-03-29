from django.core.management.base import BaseCommand
from core.models import Question, Option

class Command(BaseCommand):
    help = 'Load comprehensive psychometric questions database'

    def handle(self, *args, **options):
        # Clear existing questions
        Question.objects.all().delete()
        
        # Aptitude Questions (30)
        aptitude_questions = [
            # Logical Reasoning (10)
            {
                'text': 'What comes next in the series: 2, 6, 12, 20, ?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('28', 5),
                    ('30', 3),
                    ('26', 2),
                    ('32', 1)
                ]
            },
            {
                'text': 'If all cats are animals, and some animals are wild, which conclusion is valid?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Some cats might be wild', 5),
                    ('All cats are wild', 1),
                    ('No cats are wild', 1),
                    ('All wild animals are cats', 1)
                ]
            },
            {
                'text': 'Find the odd one out: Apple, Banana, Carrot, Mango',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Carrot', 5),
                    ('Apple', 2),
                    ('Banana', 2),
                    ('Mango', 2)
                ]
            },
            {
                'text': 'If A=1, B=2, C=3, what does CODE equal?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('60', 5),
                    ('45', 3),
                    ('50', 2),
                    ('55', 1)
                ]
            },
            {
                'text': 'A person walks 5km north, then turns right and walks 3km, then turns right again and walks 5km. Where are they facing?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('South', 5),
                    ('North', 2),
                    ('East', 2),
                    ('West', 2)
                ]
            },
            {
                'text': 'All books are pages. Some pages have pictures. Therefore:',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Some books might have pictures', 5),
                    ('All books have pictures', 1),
                    ('No books have pictures', 1),
                    ('Pages are books', 1)
                ]
            },
            {
                'text': 'Pointing to a photo, a man says "Her mother is the only daughter of my mother". How is the person in photo related to him?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Daughter', 5),
                    ('Sister', 3),
                    ('Niece', 2),
                    ('Mother', 1)
                ]
            },
            {
                'text': 'Complete the analogy: Dog : Bark :: Cat : ?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('Meow', 5),
                    ('Roar', 2),
                    ('Chirp', 2),
                    ('Growl', 2)
                ]
            },
            {
                'text': 'Which number should replace the question mark: 1, 4, 9, 16, ?',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('25', 5),
                    ('20', 3),
                    ('30', 2),
                    ('36', 1)
                ]
            },
            {
                'text': 'If Monday is to Tuesday as January is to:',
                'trait': 'logical',
                'is_mcq': True,
                'options': [
                    ('February', 5),
                    ('December', 2),
                    ('March', 2),
                    ('June', 2)
                ]
            },
            
            # Quantitative (10)
            {
                'text': 'What is 20% of 150?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('30', 5),
                    ('25', 3),
                    ('35', 2),
                    ('20', 1)
                ]
            },
            {
                'text': 'A shopkeeper bought an item for $80 and sold it for $100. What is the profit percentage?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('25%', 5),
                    ('20%', 3),
                    ('30%', 2),
                    ('15%', 1)
                ]
            },
            {
                'text': 'If a car travels 60km in 2 hours, what is its average speed?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('30 km/h', 5),
                    ('20 km/h', 3),
                    ('40 km/h', 2),
                    ('60 km/h', 1)
                ]
            },
            {
                'text': 'The ratio of boys to girls in a class is 3:2. If there are 30 students total, how many boys are there?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('18', 5),
                    ('12', 3),
                    ('15', 2),
                    ('20', 1)
                ]
            },
            {
                'text': 'What is the average of 15, 25, 35, 45?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('30', 5),
                    ('25', 3),
                    ('35', 2),
                    ('40', 1)
                ]
            },
            {
                'text': 'If $1000 is invested at 5% simple interest for 2 years, what is the total amount?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('$1100', 5),
                    ('$1000', 2),
                    ('$1050', 3),
                    ('$1200', 1)
                ]
            },
            {
                'text': 'A price increased from $50 to $60. What is the percentage increase?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('20%', 5),
                    ('10%', 3),
                    ('25%', 2),
                    ('15%', 1)
                ]
            },
            {
                'text': 'If 5 workers can complete a job in 10 days, how many days will 10 workers take?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('5 days', 5),
                    ('10 days', 2),
                    ('15 days', 2),
                    ('20 days', 1)
                ]
            },
            {
                'text': 'What is 15% of 200?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('30', 5),
                    ('25', 3),
                    ('35', 2),
                    ('20', 1)
                ]
            },
            {
                'text': 'The sum of three consecutive numbers is 72. What is the middle number?',
                'trait': 'quantitative',
                'is_mcq': True,
                'options': [
                    ('24', 5),
                    ('23', 3),
                    ('25', 2),
                    ('22', 1)
                ]
            },
            
            # Analytical (10)
            {
                'text': 'Five people are sitting in a row. A is to the left of B, C is to the right of B, D is between A and B, E is at the right end. Who is in the middle?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('B', 5),
                    ('A', 2),
                    ('C', 2),
                    ('D', 2)
                ]
            },
            {
                'text': 'In a certain code, COMPUTER is written as RFUVQNPC. How is MEDICINE written?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('MFEDKJOH', 5),
                    ('MFEJDOKH', 3),
                    ('MFEDJOKH', 2),
                    ('MFEFKJOH', 1)
                ]
            },
            {
                'text': 'A cube has 6 faces. If each face is painted and then cut into 27 smaller cubes, how many small cubes have paint on exactly 2 faces?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('12', 5),
                    ('8', 3),
                    ('6', 2),
                    ('4', 1)
                ]
            },
            {
                'text': 'If all roses are flowers and some flowers fade quickly, which statement must be true?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('Some roses might fade quickly', 5),
                    ('All roses fade quickly', 1),
                    ('No roses fade quickly', 1),
                    ('All flowers are roses', 1)
                ]
            },
            {
                'text': 'A clock shows 3:15. What is the angle between the hour and minute hands?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('7.5 degrees', 5),
                    ('0 degrees', 2),
                    ('15 degrees', 3),
                    ('30 degrees', 1)
                ]
            },
            {
                'text': 'In a group of 100 people, 70 speak English, 60 speak Hindi, and 30 speak both. How many speak at least one language?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('100', 5),
                    ('70', 2),
                    ('130', 2),
                    ('40', 1)
                ]
            },
            {
                'text': 'If the pattern is 2, 6, 12, 20, 30, what comes next?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('42', 5),
                    ('40', 3),
                    ('36', 2),
                    ('48', 1)
                ]
            },
            {
                'text': 'A statement is followed by two assumptions. Which assumption is implicit?',
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
                'text': 'If RED is coded as 6, BLUE as 9, what is GREEN coded as?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('10', 5),
                    ('8', 3),
                    ('12', 2),
                    ('9', 1)
                ]
            },
            {
                'text': 'A company has 8 departments. Each department has 5 managers and 20 employees. Total people in company?',
                'trait': 'analytical',
                'is_mcq': True,
                'options': [
                    ('200', 5),
                    ('160', 3),
                    ('180', 2),
                    ('240', 1)
                ]
            }
        ]

        # Interest Questions (35) - RIASEC
        interest_questions = [
            # Realistic (R) - 5 questions
            {
                'text': 'I enjoy working with tools or machines',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I like fixing things that are broken',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I prefer physical work over desk jobs',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I enjoy outdoor activities',
                'trait': 'R',
                'is_mcq': False
            },
            {
                'text': 'I like building or assembling things',
                'trait': 'R',
                'is_mcq': False
            },
            
            # Investigative (I) - 6 questions
            {
                'text': 'I enjoy solving complex problems',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I like science experiments',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I enjoy research work',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I like analyzing data',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I enjoy logical challenges',
                'trait': 'I',
                'is_mcq': False
            },
            {
                'text': 'I like mathematics',
                'trait': 'I',
                'is_mcq': False
            },
            
            # Artistic (A) - 6 questions
            {
                'text': 'I enjoy drawing or painting',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I like creative writing',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I enjoy designing things',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I prefer creativity over rules',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I like music or performance',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I enjoy expressing myself artistically',
                'trait': 'A',
                'is_mcq': False
            },
            
            # Social (S) - 6 questions
            {
                'text': 'I like helping people',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I enjoy teaching others',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I prefer teamwork over individual work',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I like counseling people',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I enjoy social activities',
                'trait': 'S',
                'is_mcq': False
            },
            {
                'text': 'I like working with people',
                'trait': 'S',
                'is_mcq': False
            },
            
            # Enterprising (E) - 6 questions
            {
                'text': 'I like leading teams',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I enjoy business ideas',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like taking risks',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I enjoy persuading people',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like managing things',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I prefer leadership roles',
                'trait': 'E',
                'is_mcq': False
            },
            
            # Conventional (C) - 6 questions
            {
                'text': 'I like organizing data',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I prefer structured tasks',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I like working with numbers',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I enjoy routine work',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I like planning and scheduling',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I prefer clear instructions',
                'trait': 'C',
                'is_mcq': False
            }
        ]

        # Personality Questions (35) - Big Five
        personality_questions = [
            # Openness (O) - 7 questions
            {
                'text': 'I enjoy trying new things',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I am curious about many topics',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I like creative ideas',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I enjoy abstract thinking',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I like exploring new concepts',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I prefer variety over routine',
                'trait': 'O',
                'is_mcq': False
            },
            {
                'text': 'I enjoy artistic experiences',
                'trait': 'O',
                'is_mcq': False
            },
            
            # Conscientiousness (C) - 7 questions
            {
                'text': 'I am disciplined',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I complete tasks on time',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I plan before acting',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I am organized',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I focus on goals',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I pay attention to details',
                'trait': 'C',
                'is_mcq': False
            },
            {
                'text': 'I follow schedules',
                'trait': 'C',
                'is_mcq': False
            },
            
            # Extraversion (E) - 7 questions
            {
                'text': 'I enjoy social gatherings',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like meeting new people',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I feel energized around others',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I like speaking in public',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I enjoy group activities',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I am talkative',
                'trait': 'E',
                'is_mcq': False
            },
            {
                'text': 'I prefer being with people',
                'trait': 'E',
                'is_mcq': False
            },
            
            # Agreeableness (A) - 7 questions
            {
                'text': 'I trust people easily',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I am cooperative',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I help others',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I avoid conflicts',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I am empathetic',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I am patient with others',
                'trait': 'A',
                'is_mcq': False
            },
            {
                'text': 'I consider others feelings',
                'trait': 'A',
                'is_mcq': False
            },
            
            # Neuroticism (N) - 7 questions
            {
                'text': 'I get stressed easily',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I worry a lot',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I feel anxious',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I overthink situations',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I get emotional quickly',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I am sensitive to criticism',
                'trait': 'N',
                'is_mcq': False
            },
            {
                'text': 'I mood swings frequently',
                'trait': 'N',
                'is_mcq': False
            }
        ]

        # Load Aptitude Questions
        for q_data in aptitude_questions:
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

        # Load Interest Questions
        for q_data in interest_questions:
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

        # Load Personality Questions
        for q_data in personality_questions:
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

        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(aptitude_questions)} aptitude, {len(interest_questions)} interest, and {len(personality_questions)} personality questions')
        )
