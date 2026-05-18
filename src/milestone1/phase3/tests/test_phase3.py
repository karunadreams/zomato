import pytest
from milestone1.phase1.models import Restaurant
from milestone1.phase2.models import UserPreferences
from ..service import filter_restaurants
from ..prompt_builder import build_prompt_payload

@pytest.fixture
def sample_restaurants():
    return [
        Restaurant(name="R1", address="A1", city="Delhi", cuisines=["Italian"], cost_for_two=400, rating=4.5, budget_band="Low"),
        Restaurant(name="R2", address="A2", city="Delhi", cuisines=["Chinese"], cost_for_two=800, rating=4.0, budget_band="Medium"),
        Restaurant(name="R3", address="A3", city="Bangalore", cuisines=["Italian"], cost_for_two=400, rating=4.2, budget_band="Low"),
    ]

def test_filter_by_city(sample_restaurants):
    prefs = UserPreferences(city="Delhi", budget="Low", cuisines=[], min_rating=0.0)
    results = filter_restaurants(sample_restaurants, prefs)
    assert len(results) == 1
    assert results[0].name == "R1"

def test_filter_by_rating(sample_restaurants):
    prefs = UserPreferences(city="Delhi", budget="Medium", cuisines=[], min_rating=4.2)
    results = filter_restaurants(sample_restaurants, prefs)
    assert len(results) == 0 # R2 is 4.0

def test_filter_by_cuisine(sample_restaurants):
    prefs = UserPreferences(city="Delhi", budget="Low", cuisines=["Italian"], min_rating=0.0)
    results = filter_restaurants(sample_restaurants, prefs)
    assert len(results) == 1
    assert results[0].name == "R1"

def test_prompt_builder_structure(sample_restaurants):
    prefs = UserPreferences(city="Delhi", budget="Low", cuisines=["Italian"], min_rating=0.0)
    candidates = [sample_restaurants[0]]
    payload = build_prompt_payload(prefs, candidates)
    
    assert "system" in payload
    assert "user" in payload
    assert "R1" in payload["user"]
    assert "Helpful Food Expert" in payload["system"]
