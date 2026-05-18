import pytest
from ..validator import preferences_from_mapping

def test_valid_preferences():
    data = {
        "city": "bangalore",
        "budget": "high",
        "cuisines": "Italian, Chinese",
        "min_rating": 4.0
    }
    
    prefs, errors = preferences_from_mapping(data)
    
    assert errors is None
    assert prefs is not None
    assert prefs.city == "Bangalore"
    assert prefs.budget == "High"
    assert prefs.cuisines == ["Italian", "Chinese"]
    assert prefs.min_rating == 4.0

def test_invalid_preferences():
    data = {
        "city": "",
        "budget": "Very High",
        "min_rating": 6.0
    }
    
    prefs, errors = preferences_from_mapping(data)
    
    assert prefs is None
    assert errors is not None
    assert "city" not in errors  # City/locality is optional, so an empty value is valid!
    assert "budget" in errors
    assert "min_rating" in errors
