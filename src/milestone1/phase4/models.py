from typing import List, Optional
from pydantic import BaseModel, Field

class Recommendation(BaseModel):
    name: str = Field(..., description="Name of the restaurant.")
    reasoning: str = Field(..., description="Why this restaurant was recommended.")
    score: float = Field(..., ge=0, le=1.0, description="Recommendation confidence score (0-1).")
    city: Optional[str] = Field(None, description="City/locality of the restaurant.")
    cuisines: Optional[List[str]] = Field(None, description="List of cuisines.")
    cost_for_two: Optional[int] = Field(None, description="Approximate cost for two.")
    rating: Optional[float] = Field(None, description="Restaurant rating.")

class RecommendationResponse(BaseModel):
    recommendations: List[Recommendation]
    summary: str = Field(..., description="Overall summary of the recommendation set.")
