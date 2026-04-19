# Career Logic for School Students (Class 10 Stream Selection)

import json
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key="AIzaSyDiA7IsFXYh2lJ5I78p7ktIkn1G5SHj4Qk")
model = genai.GenerativeModel('gemini-2.5-flash')

# School-specific traits
SCHOOL_TRAITS = {
    "analytical": 0,
    "biological_interest": 0,
    "business_interest": 0,
    "humanities_interest": 0
}

# Map traits to streams
STREAM_MAP = {
    "PCM": ["analytical"],
    "PCB": ["biological_interest"],
    "Commerce": ["business_interest", "analytical"],
    "Arts": ["humanities_interest"]
}

def calculate_stream_scores(responses):
    """Calculate scores for each stream based on student responses"""
    trait_scores = {
        "analytical": 0,
        "biological_interest": 0,
        "business_interest": 0,
        "humanities_interest": 0
    }
    
    # Count responses per trait
    trait_counts = {trait: 0 for trait in trait_scores.keys()}
    
    for response in responses:
        question = response['question']
        answer = response['answer']
        trait = question['trait']
        
        # Convert Likert scale to numeric values
        if answer == "Strongly Agree":
            score = 2
        elif answer == "Agree":
            score = 1
        elif answer == "Neutral":
            score = 0
        elif answer == "Disagree":
            score = -1
        elif answer == "Strongly Disagree":
            score = -2
        else:
            score = 0
        
        trait_scores[trait] += score
        trait_counts[trait] += 1
    
    # Normalize scores (average per trait)
    for trait in trait_scores:
        if trait_counts[trait] > 0:
            trait_scores[trait] = trait_scores[trait] / trait_counts[trait]
        else:
            trait_scores[trait] = 0
    
    # Calculate stream scores using STREAM_MAP
    stream_scores = {}
    for stream_name, required_traits in STREAM_MAP.items():
        score = 0
        for trait in required_traits:
            score += trait_scores.get(trait, 0)
        # Average score for streams with multiple traits
        if len(required_traits) > 1:
            score = score / len(required_traits)
        stream_scores[stream_name] = score
    
    return stream_scores, trait_scores

def get_top_stream(stream_scores):
    """Get the recommended stream based on scores"""
    return max(stream_scores, key=stream_scores.get)

def generate_stream_explanation(top_stream, trait_scores):
    """Generate personalized explanation for the recommended stream"""
    
    prompt = f"""
You are a professional career counselor helping a Class 10 student choose their stream.

Student Result:
Recommended Stream: {top_stream}
Trait Scores: {trait_scores}

Explain:
1. Why this stream suits the student
2. What subjects they will study
3. Future career options
4. Strengths of the student
5. Things they should be careful about

Keep explanation:
- Simple and clear
- Student-friendly (age 15-16)
- Practical, not motivational fluff

Return JSON only:
{{
"why_this_stream": "",
"subjects_overview": "",
"career_options": ["", "", ""],
"student_strengths": ["", "", ""],
"cautions": ["", "", ""]
}}
"""
    
    try:
        response = model.generate_content(prompt)
        result_text = response.text.strip()
        
        # Extract JSON from response
        if result_text.startswith('```json'):
            result_text = result_text[7:-3]
        elif result_text.startswith('```'):
            result_text = result_text[3:-3]
        
        return json.loads(result_text)
    except Exception as e:
        # If AI fails, return empty dict to prevent fallback content
        return {}


def get_career_recommendations(responses):
    """Main function to get career recommendations for school students"""
    
    # Check if responses is already trait_scores (from views.py)
    if isinstance(responses, dict):
        # Already calculated trait_scores from views.py
        trait_scores = responses
        stream_scores = responses.copy()  # Use the same data for stream_scores
    else:
        # Original logic for response dictionaries
        stream_scores, trait_scores = calculate_stream_scores(responses)
    
    # Get top stream
    top_stream = get_top_stream(stream_scores)
    
    # Generate explanation
    explanation = generate_stream_explanation(top_stream, trait_scores)
    
    return {
        "recommended_stream": top_stream,
        "stream_scores": stream_scores,
        "trait_scores": trait_scores,
        "explanation": explanation,
        "all_streams": list(STREAM_MAP.keys())
    }
