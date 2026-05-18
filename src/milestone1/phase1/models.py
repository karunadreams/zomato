from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(frozen=True)
class Restaurant:
    name: str
    address: str
    city: str
    cuisines: List[str] = field(default_factory=list)
    cost_for_two: int = 0
    rating: float = 0.0
    votes: int = 0
    budget_band: str = "Unknown"

    @classmethod
    def from_raw(cls, raw_data: dict) -> "Restaurant":
        """
        Factory method to create a Restaurant instance from raw dataset row.
        Normalizes data according to docs/dataset-contract.md.
        """
        # 1. Basic fields with defaults
        name = str(raw_data.get("name", "Unknown"))
        address = str(raw_data.get("address", ""))
        city = str(raw_data.get("location", "Unknown")).title() # Canonicalization: Title Case
        
        # 2. Cuisines: Split by comma and strip
        cuisines_raw = raw_data.get("cuisines", "")
        if cuisines_raw:
            cuisines = [c.strip() for c in str(cuisines_raw).split(",") if c.strip()]
        else:
            cuisines = []
            
        # 3. Cost for two
        try:
            cost_raw = raw_data.get("approx_cost(for two people)", "0")
            # Remove commas if present (e.g., "1,200")
            cost_for_two = int(str(cost_raw).replace(",", "").strip())
        except (ValueError, TypeError):
            cost_for_two = 0
            
        # 4. Rating (e.g., "4.1/5")
        try:
            rate_raw = raw_data.get("rate", "0")
            if isinstance(rate_raw, str):
                # Extract first part before "/"
                rate_str = rate_raw.split("/")[0].strip()
                if rate_str.lower() in ["new", "-", ""]:
                    rating = 0.0
                else:
                    rating = float(rate_str)
            else:
                rating = float(rate_raw or 0.0)
        except (ValueError, TypeError, IndexError):
            rating = 0.0
            
        # 5. Votes
        try:
            votes = int(raw_data.get("votes", 0))
        except (ValueError, TypeError):
            votes = 0
            
        # 6. Budget Band Calculation
        if cost_for_two < 500:
            budget_band = "Low"
        elif 500 <= cost_for_two < 1500:
            budget_band = "Medium"
        else:
            budget_band = "High"
            
        return cls(
            name=name,
            address=address,
            city=city,
            cuisines=cuisines,
            cost_for_two=cost_for_two,
            rating=rating,
            votes=votes,
            budget_band=budget_band
        )
