import pytest
from ..models import Restaurant

def test_restaurant_normalization():
    raw_row = {
        "name": "Test Restaurant",
        "address": "123 Street",
        "location": "Indiranagar",
        "cuisines": "Italian, Pizza",
        "approx_cost(for two people)": "1,200",
        "rate": "4.5/5",
        "votes": "150"
    }
    
    res = Restaurant.from_raw(raw_row)
    
    assert res.name == "Test Restaurant"
    assert res.city == "Indiranagar"
    assert res.cuisines == ["Italian", "Pizza"]
    assert res.cost_for_two == 1200
    assert res.rating == 4.5
    assert res.votes == 150
    assert res.budget_band == "Medium"

def test_restaurant_normalization_missing_data():
    raw_row = {
        "name": "Empty Cafe",
        "location": "MG Road"
    }
    
    res = Restaurant.from_raw(raw_row)
    
    assert res.name == "Empty Cafe"
    assert res.cost_for_two == 0
    assert res.rating == 0.0
    assert res.cuisines == []
    assert res.budget_band == "Low"
