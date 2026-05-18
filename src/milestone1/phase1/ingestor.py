import logging
from typing import List, Optional
from datasets import load_dataset
from .models import Restaurant

logger = logging.getLogger(__name__)

DATASET_ID = "ManikaSaini/zomato-restaurant-recommendation"

def load_restaurants(limit: Optional[int] = None) -> List[Restaurant]:
    """
    Stream/Download the Zomato dataset and normalize it into Restaurant objects.
    """
    logger.info(f"Loading dataset: {DATASET_ID}")
    
    try:
        # Using stream=True for efficiency if the dataset is large, 
        # but for small/mid datasets, simple load is fine.
        dataset = load_dataset(DATASET_ID, split="train")
        
        restaurants = []
        # Convert to a list of dicts (or iterate over the dataset)
        # We'll use a slice if limit is provided
        data_iter = dataset
        if limit:
            data_iter = dataset.select(range(min(limit, len(dataset))))
            
        for row in data_iter:
            restaurants.append(Restaurant.from_raw(row))
            
        logger.info(f"Successfully loaded {len(restaurants)} restaurants.")
        return restaurants
        
    except Exception as e:
        logger.error(f"Failed to load dataset: {e}")
        raise
