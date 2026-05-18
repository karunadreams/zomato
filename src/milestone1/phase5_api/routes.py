import os
from typing import List
from fastapi import APIRouter, HTTPException
from milestone1.phase1.ingestor import load_restaurants
from milestone1.phase2.models import UserPreferences
from milestone1.phase3 import filter_restaurants, build_prompt_payload
from milestone1.phase4 import GroqRecommender, RecommendationResponse

router = APIRouter()

import sys

# In-memory cache for restaurant data to prevent redundant dataset downloads/reads
_RESTAURANTS_CACHE = None

def get_restaurants_cached():
    global _RESTAURANTS_CACHE
    # Bypass cache during unit tests to avoid cross-test contamination and allow proper mocking
    if "pytest" in sys.modules or os.getenv("TESTING") == "true":
        return load_restaurants(limit=None)
    if _RESTAURANTS_CACHE is None:
        _RESTAURANTS_CACHE = load_restaurants(limit=None)
    return _RESTAURANTS_CACHE

@router.get("/health")
def health_check():
    """Verify system health and configuration."""
    api_key_set = bool(os.getenv("GROQ_API_KEY"))
    return {
        "status": "healthy",
        "groq_configured": api_key_set,
        "engine": "Zomato AI Recommendation System"
    }

@router.get("/api/v1/localities", response_model=List[str])
def get_localities():
    """Get all unique localities from the dataset."""
    try:
        restaurants = get_restaurants_cached()
        localities = sorted(list(set(
            r.city for r in restaurants 
            if r.city and r.city not in ["None", "Unknown"]
        )))
        return localities
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch localities: {str(e)}")

@router.get("/api/v1/cuisines", response_model=List[str])
def get_cuisines():
    """Get all unique cuisines from the Zomato Bangalore dataset."""
    try:
        restaurants = get_restaurants_cached()
        unique_cuisines = set()
        for r in restaurants:
            raw_cuisines = getattr(r, "cuisines", None)
            if raw_cuisines:
                if isinstance(raw_cuisines, list):
                    for c in raw_cuisines:
                        if c.strip():
                            unique_cuisines.add(c.strip())
                elif isinstance(raw_cuisines, str):
                    for c in raw_cuisines.split(","):
                        if c.strip():
                            unique_cuisines.add(c.strip())
        return sorted(list(unique_cuisines))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch cuisines: {str(e)}")

@router.post("/api/v1/recommend", response_model=RecommendationResponse)
def get_recommendations(prefs: UserPreferences, limit: int = 15, count: int = 5):
    """
    Orchestrate the full recommendation flow from user preferences.
    """
    try:
        # 1. Load Data
        restaurants = get_restaurants_cached()
        
        # 2. Filter Candidates
        candidates = filter_restaurants(restaurants, prefs, limit=limit)
        if not candidates:
            raise HTTPException(status_code=404, detail="No restaurants found matching your filters.")
            
        # 3. Build Prompt
        payload = build_prompt_payload(prefs, candidates, top_n=count)
        
        # 4. Get AI Recommendations
        recommender = GroqRecommender()
        response = recommender.recommend(payload)
        
        # 5. Enrich Recommendations with actual data
        candidates_map = {res.name.lower(): res for res in candidates}
        for rec in response.recommendations:
            res_obj = candidates_map.get(rec.name.lower())
            if res_obj:
                rec.city = res_obj.city
                rec.cuisines = res_obj.cuisines
                rec.cost_for_two = res_obj.cost_for_two
                rec.rating = res_obj.rating
                
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recommendation Error: {str(e)}")
