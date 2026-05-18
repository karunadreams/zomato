from typing import List, Optional
from pydantic import BaseModel, Field, validator, conlist

class UserPreferences(BaseModel):
    city: Optional[str] = Field(None, description="The locality to search for restaurants. If empty, searches all localities.")
    budget: str = Field(..., description="Budget band: Low, Medium, or High.")
    cuisines: List[str] = Field(default_factory=list, description="List of preferred cuisines.")
    min_rating: float = Field(0.0, ge=0.0, le=5.0, description="Minimum restaurant rating (0-5).")
    additional_context: Optional[str] = Field(None, max_length=500, description="Any extra preferences (e.g., 'outdoor seating').")

    @validator("budget")
    def validate_budget(cls, v):
        allowed = ["Low", "Medium", "High"]
        if v.title() not in allowed:
            raise ValueError(f"Budget must be one of {allowed}")
        return v.title()

    @validator("city", pre=True)
    def validate_city(cls, v):
        if not v or not str(v).strip():
            return None
        return str(v).strip().title()

    @validator("cuisines", pre=True)
    def validate_cuisines(cls, v):
        if v is None:
            return []
        if isinstance(v, str):
            return [c.strip() for c in v.split(",") if c.strip()]
        return v
