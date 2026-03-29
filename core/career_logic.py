# Career Domain Scoring Logic

import google.generativeai as genai
import json
import random

# Configure Gemini AI
genai.configure(api_key="AIzaSyDiA7IsFXYh2lJ5I78p7ktIkn1G5SHj4Qk")
model = genai.GenerativeModel('gemini-2.5-flash')

CAREER_DOMAINS = {
    "engineering": {
        "aptitude": ["analytical", "quantitative"],
        "interest": ["I", "R"],
        "personality": {"O": 0.6, "C": 0.8}
    },
    "medical": {
        "aptitude": ["analytical"],
        "interest": ["I", "S"],
        "personality": {"A": 0.7, "C": 0.7}
    },
    "business": {
        "aptitude": ["logical"],
        "interest": ["E", "C"],
        "personality": {"E": 0.8}
    },
    "arts": {
        "aptitude": [],
        "interest": ["A"],
        "personality": {"O": 0.9}
    },
    "science": {
        "aptitude": ["analytical", "quantitative"],
        "interest": ["I"],
        "personality": {"O": 0.8, "C": 0.6}
    },
    "education": {
        "aptitude": ["logical"],
        "interest": ["S", "I"],
        "personality": {"A": 0.8, "E": 0.6}
    },
    "law": {
        "aptitude": ["logical", "analytical"],
        "interest": ["E"],
        "personality": {"E": 0.7, "C": 0.7}
    },
    "design": {
        "aptitude": ["analytical"],
        "interest": ["A", "R"],
        "personality": {"O": 0.9, "A": 0.6}
    }
}

DEGREES = {
    "engineering": [
        "B.Tech Computer Science",
        "B.Tech AI & Data Science",
        "BCA",
        "B.Tech Electrical",
        "B.Tech Civil",
        "B.Tech Chemical"
    ],
    "medical": [
        "MBBS",
        "BDS",
        "BSc Nursing",
        "BPharm",
        "BPT (Physiotherapy)",
        "BSc Medical Lab Technology"
    ],
    "business": [
        "BBA",
        "B.Com",
        "BBM",
        "BMS",
        "B.Sc. Economics",
        "B.Sc. Finance"
    ],
    "arts": [
        "BA Psychology",
        "BA English",
        "BA Sociology",
        "Bachelor of Fine Arts",
        "BA History",
        "BA Philosophy"
    ],
    "science": [
        "B.Sc. Physics",
        "B.Sc. Chemistry",
        "B.Sc. Mathematics",
        "B.Sc. Biology",
        "B.Sc. Statistics",
        "B.Sc. Computer Science"
    ],
    "education": [
        "B.Ed.",
        "BA Education",
        "B.Sc. Education",
        "Early Childhood Education",
        "Special Education"
    ],
    "law": [
        "LLB",
        "BA LLB",
        "B.Com LLB",
        "B.Sc. LLB"
    ],
    "design": [
        "B.Des. Fashion Design",
        "B.Des. Graphic Design",
        "B.Des. Interior Design",
        "B.Arch",
        "BFA (Bachelor of Fine Arts)",
        "B.Des. Industrial Design"
    ]
}

def detect_dominant_interest(interest_scores):
    """Detect the dominant interest trait and its value"""
    top_trait = max(interest_scores, key=interest_scores.get)
    top_value = interest_scores[top_trait]
    return top_trait, top_value

# DOMAIN PRIORITY BOOSTS
DOMAIN_PRIORITY = {
    "arts": 1.3,
    "design": 1.2,
    "education": 1.0,
    "business": 1.0,
}

# DOMAIN RULES (CRITICAL FILTERING)
DOMAIN_RULES = {
    "engineering": lambda s: s["aptitude"]["quantitative"] >= 30 and s["aptitude"]["analytical"] >= 30,
    "medical": lambda s: s["interest"]["I"] >= 30 and s["aptitude"]["analytical"] >= 25,
    "law": lambda s: s["aptitude"]["logical"] >= 25 and s["aptitude"]["analytical"] >= 25,
    "science": lambda s: s["aptitude"]["analytical"] >= 30,
    "business": lambda s: s["interest"]["E"] >= 20,
    "design": lambda s: s["interest"]["A"] >= 25,
    "arts": lambda s: s["interest"]["A"] >= 20,
    "education": lambda s: s["interest"]["S"] >= 60 and s["personality"]["E"] >= 60,
}

def calculate_domain_score(user_scores, domain):
    """Calculate score for a specific career domain"""
    score = 0

    # NEW WEIGHTS: Aptitude → 30%, Interest → 50%, Personality → 20%
    if domain["aptitude"]:
        apt = sum(user_scores["aptitude"].get(k, 0) for k in domain["aptitude"]) / len(domain["aptitude"])
        score += apt * 0.3  # Reduced from 0.5

    # Interest → 50% (increased from 30%)
    if domain["interest"]:
        intr = sum(user_scores["interest"].get(k, 0) for k in domain["interest"]) / len(domain["interest"])
        score += intr * 0.5  # Increased from 0.3

    # Personality → 20% (unchanged)
    pers = sum(user_scores["personality"].get(k, 0) * w for k, w in domain["personality"].items())
    score += pers * 0.2

    return score

def filter_domains(user_scores):
    """Filter domains based on minimum requirements"""
    valid = {}

    for domain, data in CAREER_DOMAINS.items():
        rule = DOMAIN_RULES.get(domain)

        if rule:
            try:
                if not rule(user_scores):
                    continue
            except:
                continue

        valid[domain] = data

    return valid

def get_degrees(domain):
    """Get 3 degrees for a single domain"""
    return DEGREES[domain][:3]  # Always first 3 degrees

def get_career_recommendations(aptitude_scores, interest_scores, personality_scores):
    """Get career recommendations with dominant interest override logic"""

    user_scores = {
        "aptitude": aptitude_scores,
        "interest": interest_scores,
        "personality": personality_scores
    }

    # STEP 1: DETECT DOMINANT INTEREST (HARD OVERRIDE LOGIC)
    dominant_trait, dominant_value = detect_dominant_interest(interest_scores)
    
    # HARD OVERRIDE: If dominant interest is very strong (>=85), force domain selection
    if dominant_value >= 85:
        if dominant_trait == "A":
            return {
                "top_domain": "arts",
                "recommended_degrees": DEGREES["arts"][:3],
                "user_scores": user_scores,
                "dominant_override": True
            }
        if dominant_trait == "S":
            return {
                "top_domain": "education",
                "recommended_degrees": DEGREES["education"][:3],
                "user_scores": user_scores,
                "dominant_override": True
            }
        if dominant_trait == "E":
            return {
                "top_domain": "business",
                "recommended_degrees": DEGREES["business"][:3],
                "user_scores": user_scores,
                "dominant_override": True
            }
        if dominant_trait == "I":
            return {
                "top_domain": "science",
                "recommended_degrees": DEGREES["science"][:3],
                "user_scores": user_scores,
                "dominant_override": True
            }

    # STEP 2: FILTER DOMAINS
    filtered_domains = filter_domains(user_scores)

    # fallback (if everything filtered)
    if not filtered_domains:
        filtered_domains = {
            "arts": CAREER_DOMAINS["arts"],
            "business": CAREER_DOMAINS["business"]
        }

    # STEP 3: CALCULATE SCORES
    domain_scores = {}
    for domain_name, domain_data in filtered_domains.items():
        score = calculate_domain_score(user_scores, domain_data)
        # Apply priority boost
        score *= DOMAIN_PRIORITY.get(domain_name, 1.0)
        domain_scores[domain_name] = score

    # STEP 4: SORT DOMAINS
    sorted_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
    
    # STEP 5: SELECT TOP DOMAIN
    top_domain = sorted_domains[0][0]
    
    # STEP 6: GET DEGREES
    degrees = get_degrees(top_domain)

    return {
        "top_domain": top_domain,
        "recommended_degrees": degrees,
        "domain_scores": dict(sorted_domains),
        "user_scores": user_scores,
        "dominant_override": False
    }

def generate_career_guidance(recommendation_data):
    """Generate comprehensive AI-powered career guidance using Gemini 2.5 Flash"""
    try:
        prompt = f"""
        You are an expert career counselor providing personalized career guidance based on psychometric assessment results. 
        Generate comprehensive, actionable insights that will help the user make informed career decisions.

        USER ASSESSMENT RESULTS:
        - Primary Career Domain: {recommendation_data['top_domain'].upper()}
        - Recommended Degrees: {', '.join(recommendation_data['recommended_degrees'])}
        
        DETAILED SCORE BREAKDOWN:
        - Aptitude Scores: {recommendation_data['user_scores']['aptitude']}
        - Interest Profile (RIASEC): {recommendation_data['user_scores']['interest']}
        - Personality Traits (Big Five): {recommendation_data['user_scores']['personality']}
        
        Domain Match Scores: {recommendation_data['domain_scores']}

        GENERATE COMPREHENSIVE GUIDANCE covering these specific areas:

        1. **WHY THIS DOMAIN FITS YOU**: 
           - Explain how your specific aptitude, interest, and personality scores align with this career domain
           - Reference your top 2-3 strongest traits and how they contribute to success in this field
           - Be specific about what makes you a good candidate

        2. **YOUR KEY STRENGTHS & ADVANTAGES**:
           - Identify 4-5 specific strengths from your assessment results
           - Explain how each strength translates to workplace advantages
           - Include both hard skills (aptitude-based) and soft skills (personality-based)

        3. **CAREER PATH & OPPORTUNITIES**:
           - For each recommended degree, provide 2-3 specific career roles
           - Include salary expectations (entry-level to mid-career)
           - Growth potential and industry demand trends
           - Required skills beyond education

        4. **EDUCATION ROADMAP**:
           - Best colleges/institutions for these degrees in India
           - Entrance exams required and preparation strategies
           - Alternative paths (online degrees, certifications, diplomas)

        5. **SKILL DEVELOPMENT PLAN**:
           - Technical skills to build during education
           - Soft skills to develop for career success
           - Certifications and internships that add value
           - Timeline for skill acquisition

        6. **INDUSTRY INSIGHTS**:
           - Current market demand and future growth projections
           - Top companies hiring in this domain
           - Work environment and culture expectations
           - Challenges and how to prepare for them

        7. **ACTIONABLE NEXT STEPS**:
           - Immediate actions (next 1-3 months)
           - Short-term goals (3-12 months)
           - Long-term planning (1-3 years)
           - Resources for further exploration

        REQUIREMENTS:
        - Use black and white color scheme only (no colors in the response)
        - Be encouraging but realistic
        - Provide specific, actionable advice
        - Include current industry trends and data
        - Format as structured JSON with proper keys
        - Keep language professional yet accessible
        - Focus on Indian education system and job market

        Format your response as JSON with these exact keys:
        {{
            "why_this_fits": "detailed explanation",
            "key_strengths": ["strength1", "strength2", "strength3", "strength4"],
            "career_opportunities": {{
                "degree1": {{
                    "careers": ["role1", "role2", "role3"],
                    "salary_range": "entry to mid-level",
                    "growth_potential": "description",
                    "industry_demand": "high/medium/low"
                }}
            }},
            "education_roadmap": {{
                "top_colleges": ["college1", "college2", "college3"],
                "entrance_exams": ["exam1", "exam2"],
                "preparation_tips": ["tip1", "tip2", "tip3"],
                "alternative_paths": ["path1", "path2"]
            }},
            "skill_development": {{
                "technical_skills": ["skill1", "skill2", "skill3"],
                "soft_skills": ["skill1", "skill2", "skill3"],
                "certifications": ["cert1", "cert2"],
                "internship_opportunities": ["opp1", "opp2"]
            }},
            "industry_insights": {{
                "market_demand": "current and future trends",
                "top_companies": ["company1", "company2", "company3"],
                "work_environment": "description",
                "challenges": ["challenge1", "challenge2"]
            }},
            "action_steps": {{
                "immediate": ["action1", "action2"],
                "short_term": ["goal1", "goal2"],
                "long_term": ["goal1", "goal2"],
                "resources": ["resource1", "resource2", "resource3"]
            }}
        }}
        """
        
        response = model.generate_content(prompt)
        guidance_text = response.text
        
        # Try to parse as JSON, fallback to structured response if parsing fails
        try:
            return json.loads(guidance_text)
        except Exception as e:
            # Fallback structured response
            return {
                "why_this_fits": f"Based on your assessment results, {recommendation_data['top_domain']} aligns perfectly with your aptitude scores, interest profile, and personality traits. Your strongest areas complement the requirements of this career domain.",
                "key_strengths": [
                    "Strong analytical thinking abilities",
                    "Excellent problem-solving skills", 
                    "High adaptability and learning capacity",
                    "Natural leadership potential"
                ],
                "career_opportunities": {
                    recommendation_data['recommended_degrees'][0]: {
                        "careers": ["Entry-level position", "Mid-level specialist", "Senior expert"],
                        "salary_range": "3-8 LPA entry level to 15-25 LPA mid-career",
                        "growth_potential": "High growth potential with experience",
                        "industry_demand": "High demand in current market"
                    }
                },
                "education_roadmap": {
                    "top_colleges": ["Tier 1 institutions", "Reputed private universities"],
                    "entrance_exams": ["National level entrance exams", "State-level exams"],
                    "preparation_tips": ["Start early preparation", "Focus on fundamentals", "Practice mock tests"],
                    "alternative_paths": ["Online degree programs", "Professional certifications"]
                },
                "skill_development": {
                    "technical_skills": ["Core domain knowledge", "Digital literacy", "Analytical tools"],
                    "soft_skills": ["Communication", "Teamwork", "Leadership"],
                    "certifications": ["Industry-recognized certifications"],
                    "internship_opportunities": ["Industry internships", "Research projects"]
                },
                "industry_insights": {
                    "market_demand": "Growing demand with digital transformation",
                    "top_companies": ["Leading industry players", "Startups", "MNCs"],
                    "work_environment": "Dynamic and collaborative environment",
                    "challenges": ["Continuous learning requirement", "Competition"]
                },
                "action_steps": {
                    "immediate": ["Research degree programs", "Connect with professionals"],
                    "short_term": ["Prepare for entrance exams", "Build relevant skills"],
                    "long_term": ["Complete education", "Gain work experience"],
                    "resources": ["Educational websites", "Industry publications", "Professional networks"]
                }
            }
    except Exception as e:
        # Comprehensive fallback guidance if AI fails
        return {
            "why_this_fits": f"Your assessment results indicate strong alignment with {recommendation_data['top_domain']}. Your aptitude scores, interest profile, and personality traits create an excellent foundation for success in this career domain.",
            "key_strengths": [
                "Analytical and logical reasoning abilities",
                "Strong problem-solving capabilities",
                "Adaptability and quick learning",
                "Natural aptitude for this domain"
            ],
            "career_opportunities": {
                recommendation_data['recommended_degrees'][0]: {
                    "careers": ["Junior Associate", "Team Lead", "Department Head"],
                    "salary_range": "2.5-6 LPA entry level to 12-20 LPA experienced",
                    "growth_potential": "Excellent growth trajectory with specialization",
                    "industry_demand": "Steady demand with future growth potential"
                }
            },
            "education_roadmap": {
                "top_colleges": ["Reputed government colleges", "Established private universities"],
                "entrance_exams": ["National entrance tests", "University-specific exams"],
                "preparation_tips": "Focus on conceptual understanding and regular practice",
                "alternative_paths": ["Distance education", "Professional diploma programs"]
            },
            "skill_development": {
                "technical_skills": ["Domain-specific knowledge", "Computer proficiency"],
                "soft_skills": ["Communication skills", "Team collaboration"],
                "certifications": ["Industry-standard certifications"],
                "internship_opportunities": ["Summer internships", "Industry projects"]
            },
            "industry_insights": {
                "market_demand": "Consistent demand with technological evolution",
                "top_companies": ["Established corporations", "Growing organizations"],
                "work_environment": "Professional environment with growth opportunities",
                "challenges": ["Need for continuous upskilling", "Industry competition"]
            },
            "action_steps": {
                "immediate": ["Research educational options", "Speak with industry professionals"],
                "short_term": ["Begin exam preparation", "Develop foundational skills"],
                "long_term": ["Complete degree program", "Build professional network"],
                "resources": ["Educational portals", "Industry reports", "Mentorship programs"]
            }
        }
