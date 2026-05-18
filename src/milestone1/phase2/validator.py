from typing import Any, Dict, Tuple, Optional
from pydantic import ValidationError
from .models import UserPreferences

def preferences_from_mapping(data: Dict[str, Any]) -> Tuple[Optional[UserPreferences], Optional[Dict[str, str]]]:
    """
    Validates input mapping and returns a UserPreferences object or a dict of field errors.
    Returns (preferences, errors).
    """
    try:
        prefs = UserPreferences(**data)
        return prefs, None
    except ValidationError as e:
        # Simplify Pydantic errors for the UI/CLI
        errors = {err["loc"][0]: err["msg"] for err in e.errors()}
        return None, errors
