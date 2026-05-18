import json
from typing import List, Dict
from milestone1.phase1.models import Restaurant
from milestone1.phase2.models import UserPreferences

SYSTEM_PROMPT = """You are a Helpful Food Expert and Restaurant Recommender. 
Your goal is to help users find the top {top_n} restaurants from a provided list based on their specific preferences.

GROUNDING RULES:
1. ONLY recommend restaurants from the provided candidate list.
2. Provide EXACTLY {top_n} recommendations if enough candidates match. If not enough candidates match perfectly, provide as many as possible that are reasonable.
3. If no restaurants fit the criteria, politely explain why and suggest what might be a close match or ask for broader criteria.
4. For each recommendation, provide a "personalized justification" that references the user's preferences (e.g., matching cuisine, budget, or additional context).
5. Do not make up information about the restaurants.

OUTPUT FORMAT:
Return a JSON object with:
{{
  "recommendations": [
    {{
      "name": "Restaurant Name",
      "reasoning": "Why this is a good fit...",
      "score": 0.95
    }}
  ],
  "summary": "Overall summary of why these picks were chosen."
}}
"""

def build_prompt_payload(prefs: UserPreferences, candidates: List[Restaurant], top_n: int = 5) -> Dict:
    """
    Construct the final prompt payload for the LLM.
    """
    # Convert candidates to a simplified JSON-friendly format for the prompt
    candidate_list = []
    for res in candidates:
        candidate_list.append({
            "name": res.name,
            "city": res.city,
            "cuisines": res.cuisines,
            "cost_for_two": res.cost_for_two,
            "rating": res.rating,
            "votes": res.votes,
            "budget_band": res.budget_band
        })
        
    user_message = {
        "user_preferences": {
            "city": prefs.city if prefs.city else "Any Locality",
            "budget": prefs.budget,
            "preferred_cuisines": prefs.cuisines if prefs.cuisines else "All Cuisines",
            "min_rating": prefs.min_rating,
            "additional_context": prefs.additional_context if prefs.additional_context else "None"
        },
        "candidate_restaurants": candidate_list
    }
    
    return {
        "system": SYSTEM_PROMPT.format(top_n=top_n),
        "user": json.dumps(user_message, indent=2)
    }
