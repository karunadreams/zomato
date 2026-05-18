from typing import List
import logging
from milestone1.phase1.models import Restaurant
from milestone1.phase2.models import UserPreferences

logger = logging.getLogger(__name__)

def filter_restaurants(restaurants: List[Restaurant], prefs: UserPreferences, limit: int = 15) -> List[Restaurant]:
    """
    Apply deterministic filters based on user preferences.
    """
    logger.info(f"Filtering {len(restaurants)} restaurants for city: {prefs.city}")
    
    candidates = []
    
    for res in restaurants:
        # 1. City filter (Smart matching: e.g. "Koramangala" matches "Koramangala 5th Block", "Whitefield" matches "Itpl Main Road, Whitefield")
        if prefs.city:
            pref_city_normalized = prefs.city.lower().replace(" layout", "").strip()
            res_city_normalized = res.city.lower().replace(" layout", "").strip()
            if pref_city_normalized not in res_city_normalized and res_city_normalized not in pref_city_normalized:
                continue
            
        # 2. Rating filter (>= min_rating)
        if res.rating < prefs.min_rating:
            continue
            
        # 3. Budget filter (Exact match with band)
        if res.budget_band != prefs.budget:
            continue
            
        # 4. Cuisine filter (Overlap if prefs.cuisines is not empty)
        if prefs.cuisines:
            res_cuisines_set = {c.lower() for c in res.cuisines}
            prefs_cuisines_set = {c.lower() for c in prefs.cuisines}
            if not res_cuisines_set.intersection(prefs_cuisines_set):
                continue
                
        candidates.append(res)
        
    # 5. Deduplicate by name (keeping the one with higher rating/votes if duplicates exist)
    unique_candidates = {}
    for res in candidates:
        if res.name not in unique_candidates or res.rating > unique_candidates[res.name].rating:
            unique_candidates[res.name] = res
    
    final_list = list(unique_candidates.values())
    
    # 6. Ranking hint: Sort by rating (descending)
    final_list.sort(key=lambda x: x.rating, reverse=True)
    
    # 7. Apply limit
    final_candidates = final_list[:limit]
    logger.info(f"Filter complete. Found {len(final_candidates)} candidates.")
    
    return final_candidates
