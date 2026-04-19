from django.core.management.base import BaseCommand
from core.models import SchoolQuestion
import random

class Command(BaseCommand):
    help = 'Add 30 comprehensive questions for each stream (PCM, PCB, Commerce, Arts)'

    def handle(self, *args, **options):
        # Clear existing questions
        SchoolQuestion.objects.all().delete()
        
        # PCM Questions (30)
        pcm_questions = [
            {
                'text': 'What is the derivative of x²?',
                'options': ['2x', 'x²', 'x', '2'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the acceleration due to gravity on Earth?',
                'options': ['9.8 m/s²', '10 m/s²', '8.5 m/s²', '12 m/s²'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the chemical formula for water?',
                'options': ['H2O', 'CO2', 'O2', 'H2'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the value of sin(90°)?',
                'options': ['1', '0', '0.5', '2'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the unit of force?',
                'options': ['Newton', 'Joule', 'Watt', 'Pascal'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the atomic number of Carbon?',
                'options': ['6', '8', '12', '4'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the integral of 2x?',
                'options': ['x² + C', '2x²', 'x', '2x + C'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the speed of light in vacuum?',
                'options': ['3×10^8 m/s', '2×10^8 m/s', '4×10^8 m/s', '1×10^8 m/s'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the pH of pure water?',
                'options': ['7', '0', '14', '1'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the logarithm of 100 to base 10?',
                'options': ['2', '10', '100', '1'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the unit of electric current?',
                'options': ['Ampere', 'Volt', 'Ohm', 'Watt'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the molecular weight of O2?',
                'options': ['32', '16', '64', '8'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the value of cos(0°)?',
                'options': ['1', '0', '0.5', '2'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the unit of power?',
                'options': ['Watt', 'Joule', 'Newton', 'Pascal'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the chemical symbol for Gold?',
                'options': ['Au', 'Ag', 'Fe', 'Cu'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the value of e (Euler\'s number)?',
                'options': ['2.718', '3.141', '1.618', '2.236'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the unit of energy?',
                'options': ['Joule', 'Newton', 'Watt', 'Pascal'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the chemical formula for carbon dioxide?',
                'options': ['CO2', 'O2', 'H2O', 'N2'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the value of tan(45°)?',
                'options': ['1', '0', 'undefined', '2'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the unit of resistance?',
                'options': ['Ohm', 'Volt', 'Ampere', 'Watt'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the atomic number of Oxygen?',
                'options': ['8', '6', '16', '12'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the derivative of sin(x)?',
                'options': ['cos(x)', '-cos(x)', 'sin(x)', '-sin(x)'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the unit of pressure?',
                'options': ['Pascal', 'Newton', 'Joule', 'Watt'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the chemical formula for methane?',
                'options': ['CH4', 'CO2', 'H2O', 'NH3'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the value of log(1)?',
                'options': ['0', '1', '10', 'undefined'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the unit of frequency?',
                'options': ['Hertz', 'Newton', 'Joule', 'Watt'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the chemical symbol for Silver?',
                'options': ['Ag', 'Au', 'Fe', 'Cu'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the value of 2^5?',
                'options': ['32', '16', '64', '8'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the unit of magnetic field?',
                'options': ['Tesla', 'Newton', 'Joule', 'Watt'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the chemical formula for ammonia?',
                'options': ['NH3', 'CH4', 'CO2', 'H2O'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the value of 5! (5 factorial)?',
                'options': ['120', '60', '25', '100'],
                'correct': 'A',
                'step': 1
            }
        ]

        # PCB Questions (30)
        pcb_questions = [
            {
                'text': 'What is the powerhouse of the cell?',
                'options': ['Mitochondria', 'Nucleus', 'Ribosome', 'Golgi apparatus'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the acceleration due to gravity on Earth?',
                'options': ['9.8 m/s²', '10 m/s²', '8.5 m/s²', '12 m/s²'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the chemical formula for glucose?',
                'options': ['C6H12O6', 'CO2', 'H2O', 'O2'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the function of red blood cells?',
                'options': ['Carry oxygen', 'Fight infection', 'Clot blood', 'Produce hormones'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the unit of force?',
                'options': ['Newton', 'Joule', 'Watt', 'Pascal'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the process of photosynthesis?',
                'options': ['Converting light energy to chemical energy', 'Breaking down food', 'Removing waste', 'Pumping blood'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the function of the heart?',
                'options': ['Pump blood', 'Filter blood', 'Digest food', 'Produce hormones'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the speed of light in vacuum?',
                'options': ['3×10^8 m/s', '2×10^8 m/s', '4×10^8 m/s', '1×10^8 m/s'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the function of the kidneys?',
                'options': ['Filter blood', 'Digest food', 'Pump blood', 'Produce hormones'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the function of the lungs?',
                'options': ['Exchange gases', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the unit of electric current?',
                'options': ['Ampere', 'Volt', 'Ohm', 'Watt'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the function of the brain?',
                'options': ['Control body functions', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the function of the liver?',
                'options': ['Detoxification', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the unit of power?',
                'options': ['Watt', 'Joule', 'Newton', 'Pascal'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the function of DNA?',
                'options': ['Store genetic information', 'Protein synthesis', 'Energy production', 'Waste removal'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the function of RNA?',
                'options': ['Protein synthesis', 'Store genetic information', 'Energy production', 'Waste removal'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the function of enzymes?',
                'options': ['Catalyze reactions', 'Store energy', 'Transport oxygen', 'Fight infection'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the function of the stomach?',
                'options': ['Digest food', 'Pump blood', 'Filter waste', 'Produce hormones'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the function of the intestines?',
                'options': ['Absorb nutrients', 'Pump blood', 'Filter waste', 'Produce hormones'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the function of the pancreas?',
                'options': ['Produce insulin', 'Pump blood', 'Filter waste', 'Digest food'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the function of white blood cells?',
                'options': ['Fight infection', 'Carry oxygen', 'Clot blood', 'Produce hormones'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the function of platelets?',
                'options': ['Clot blood', 'Carry oxygen', 'Fight infection', 'Produce hormones'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the function of the nervous system?',
                'options': ['Control body functions', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the function of the endocrine system?',
                'options': ['Produce hormones', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the function of the immune system?',
                'options': ['Fight disease', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is the function of the skeletal system?',
                'options': ['Support body', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is the function of the muscular system?',
                'options': ['Movement', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is the function of the circulatory system?',
                'options': ['Transport blood', 'Digest food', 'Filter waste', 'Produce hormones'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is the function of the respiratory system?',
                'options': ['Exchange gases', 'Pump blood', 'Digest food', 'Filter waste'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is the function of the digestive system?',
                'options': ['Break down food', 'Pump blood', 'Filter waste', 'Produce hormones'],
                'correct': 'A',
                'step': 5
            }
        ]

        # Commerce Questions (30)
        commerce_questions = [
            {
                'text': 'What is the accounting equation?',
                'options': ['Assets = Liabilities + Equity', 'Assets = Liabilities - Equity', 'Assets + Liabilities = Equity', 'Assets - Liabilities = Equity'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is GDP?',
                'options': ['Total value of goods and services', 'Total income', 'Total exports', 'Total imports'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is profit?',
                'options': ['Revenue - Expenses', 'Revenue + Expenses', 'Expenses - Revenue', 'Revenue × Expenses'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is demand?',
                'options': ['Willingness to buy', 'Ability to sell', 'Price of goods', 'Quantity supplied'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is supply?',
                'options': ['Quantity available', 'Quantity demanded', 'Price of goods', 'Market size'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is inflation?',
                'options': ['Rise in prices', 'Fall in prices', 'Stable prices', 'No price change'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is a balance sheet?',
                'options': ['Financial statement', 'Income statement', 'Cash flow statement', 'Profit statement'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is an income statement?',
                'options': ['Revenue and expenses', 'Assets and liabilities', 'Cash flows', 'Equity changes'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is cash flow?',
                'options': ['Movement of money', 'Profit', 'Revenue', 'Expenses'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is interest?',
                'options': ['Cost of borrowing', 'Cost of selling', 'Cost of producing', 'Cost of marketing'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is a loan?',
                'options': ['Borrowed money', 'Saved money', 'Invested money', 'Earned money'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is investment?',
                'options': ['Putting money to work', 'Saving money', 'Spending money', 'Borrowing money'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is a market?',
                'options': ['Place for buying and selling', 'Place for production', 'Place for storage', 'Place for distribution'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is competition?',
                'options': ['Rivalry among sellers', 'Cooperation among sellers', 'Monopoly of sellers', 'Agreement among sellers'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is monopoly?',
                'options': ['Single seller', 'Many sellers', 'Few sellers', 'No sellers'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is revenue?',
                'options': ['Total income', 'Total profit', 'Total expenses', 'Total assets'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is expense?',
                'options': ['Cost of operations', 'Income', 'Profit', 'Revenue'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is capital?',
                'options': ['Money for investment', 'Money for consumption', 'Money for saving', 'Money for borrowing'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is a budget?',
                'options': ['Financial plan', 'Financial statement', 'Financial report', 'Financial analysis'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is audit?',
                'options': ['Financial examination', 'Financial planning', 'Financial reporting', 'Financial analysis'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is tax?',
                'options': ['Government charge', 'Business charge', 'Personal charge', 'Bank charge'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is insurance?',
                'options': ['Risk protection', 'Investment', 'Saving', 'Loan'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is banking?',
                'options': ['Financial services', 'Production services', 'Marketing services', 'Distribution services'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is stock?',
                'options': ['Share of ownership', 'Loan to company', 'Deposit in bank', 'Insurance policy'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is bond?',
                'options': ['Debt instrument', 'Share of ownership', 'Bank deposit', 'Insurance policy'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is dividend?',
                'options': ['Share of profit', 'Share of revenue', 'Share of assets', 'Share of expenses'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is bankruptcy?',
                'options': ['Inability to pay debts', 'Inability to earn profit', 'Inability to sell', 'Inability to produce'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is merger?',
                'options': ['Combination of companies', 'Division of companies', 'Sale of companies', 'Purchase of companies'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is acquisition?',
                'options': ['Purchase of company', 'Sale of company', 'Merger of companies', 'Division of company'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is franchise?',
                'options': ['License to operate', 'Ownership of business', 'Partnership in business', 'Investment in business'],
                'correct': 'A',
                'step': 5
            }
        ]

        # Arts Questions (30)
        arts_questions = [
            {
                'text': 'What is literature?',
                'options': ['Written works', 'Spoken works', 'Visual works', 'Musical works'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is art?',
                'options': ['Creative expression', 'Scientific expression', 'Mathematical expression', 'Technical expression'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is culture?',
                'options': ['Way of life', 'Way of work', 'Way of study', 'Way of travel'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is society?',
                'options': ['Group of people', 'Group of animals', 'Group of plants', 'Group of objects'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is history?',
                'options': ['Study of past', 'Study of present', 'Study of future', 'Study of nature'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is geography?',
                'options': ['Study of earth', 'Study of space', 'Study of ocean', 'Study of atmosphere'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is psychology?',
                'options': ['Study of mind', 'Study of body', 'Study of society', 'Study of nature'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is sociology?',
                'options': ['Study of society', 'Study of mind', 'Study of body', 'Study of nature'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is philosophy?',
                'options': ['Study of wisdom', 'Study of science', 'Study of art', 'Study of history'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is language?',
                'options': ['Communication system', 'Writing system', 'Speaking system', 'Reading system'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is religion?',
                'options': ['Belief system', 'Political system', 'Economic system', 'Social system'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is ethics?',
                'options': ['Moral principles', 'Legal principles', 'Religious principles', 'Social principles'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is politics?',
                'options': ['Governance system', 'Economic system', 'Social system', 'Cultural system'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is economics?',
                'options': ['Study of wealth', 'Study of health', 'Study of education', 'Study of environment'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is anthropology?',
                'options': ['Study of humans', 'Study of animals', 'Study of plants', 'Study of earth'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is archaeology?',
                'options': ['Study of ancient remains', 'Study of modern life', 'Study of future predictions', 'Study of space'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is linguistics?',
                'options': ['Study of language', 'Study of speech', 'Study of writing', 'Study of reading'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is music?',
                'options': ['Art of sound', 'Art of sight', 'Art of touch', 'Art of taste'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is dance?',
                'options': ['Art of movement', 'Art of sound', 'Art of sight', 'Art of speech'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is theater?',
                'options': ['Performance art', 'Visual art', 'Literary art', 'Musical art'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is painting?',
                'options': ['Visual art', 'Performance art', 'Literary art', 'Musical art'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is sculpture?',
                'options': ['3D art', '2D art', 'Digital art', 'Performance art'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is photography?',
                'options': ['Image capture', 'Image creation', 'Image editing', 'Image display'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is film?',
                'options': ['Moving pictures', 'Still pictures', 'Drawn pictures', 'Digital pictures'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is journalism?',
                'options': ['News reporting', 'Story writing', 'Poetry writing', 'Novel writing'],
                'correct': 'A',
                'step': 5
            },
            {
                'text': 'What is education?',
                'options': ['Learning process', 'Teaching process', 'Working process', 'Playing process'],
                'correct': 'A',
                'step': 1
            },
            {
                'text': 'What is communication?',
                'options': ['Information exchange', 'Information storage', 'Information processing', 'Information creation'],
                'correct': 'A',
                'step': 2
            },
            {
                'text': 'What is media?',
                'options': ['Communication channels', 'Storage devices', 'Processing tools', 'Creation tools'],
                'correct': 'A',
                'step': 3
            },
            {
                'text': 'What is entertainment?',
                'options': ['Amusement activities', 'Work activities', 'Study activities', 'Rest activities'],
                'correct': 'A',
                'step': 4
            },
            {
                'text': 'What is creativity?',
                'options': ['Original thinking', 'Memory thinking', 'Logical thinking', 'Mathematical thinking'],
                'correct': 'A',
                'step': 5
            }
        ]

        # Add all questions to database
        all_questions = [
            (pcm_questions, 'PCM'),
            (pcb_questions, 'PCB'), 
            (commerce_questions, 'Commerce'),
            (arts_questions, 'Arts')
        ]

        total_added = 0
        for questions_list, stream in all_questions:
            for q in questions_list:
                # Shuffle options to randomize correct answer position
                options = q['options'].copy()
                correct_answer = q['correct']
                correct_text = options[0]  # Original correct answer is always first option
                
                # Shuffle options
                random.shuffle(options)
                
                # Find new position of correct answer
                new_correct_pos = options.index(correct_text)
                new_correct = chr(65 + new_correct_pos)  # A, B, C, D
                
                SchoolQuestion.objects.create(
                    text=q['text'],
                    option_a=options[0],
                    option_b=options[1], 
                    option_c=options[2],
                    option_d=options[3],
                    correct_answer=new_correct,
                    step=q['step'],
                    stream_hint=stream
                )
                total_added += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully added {total_added} school questions ({len(pcm_questions)} PCM, {len(pcb_questions)} PCB, {len(commerce_questions)} Commerce, {len(arts_questions)} Arts)')
        )
