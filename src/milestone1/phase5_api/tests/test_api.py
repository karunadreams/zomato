import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from ..app import app
from milestone1.phase4.models import RecommendationResponse

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

@patch("milestone1.phase5_api.routes.load_restaurants")
@patch("milestone1.phase4.GroqRecommender.recommend")
def test_recommend_endpoint(mock_recommend, mock_load):
    # Mock data
    mock_load.return_value = [] # This will trigger the "No restaurants found" 404
    
    payload = {
        "city": "Delhi",
        "budget": "Low",
        "cuisines": ["Italian"],
        "min_rating": 4.0
    }
    
    response = client.post("/api/v1/recommend", json=payload)
    assert response.status_code == 404
    assert "No restaurants found" in response.json()["detail"]

from milestone1.phase1.models import Restaurant

@patch("milestone1.phase5_api.routes.load_restaurants")
@patch("milestone1.phase5_api.routes.GroqRecommender")
@patch("milestone1.phase5_api.routes.filter_restaurants")
def test_recommend_endpoint_success(mock_filter, mock_recommender_class, mock_load):
    # Mock success flow
    sample_resto = Restaurant(
        name="Test Resto", address="Addr", city="Delhi", 
        cuisines=["Italian"], cost_for_two=500, rating=4.5, budget_band="Medium"
    )
    mock_filter.return_value = [sample_resto]
    
    mock_instance = MagicMock()
    mock_instance.recommend.return_value = RecommendationResponse(
        recommendations=[{"name": "Test", "reasoning": "Reason", "score": 0.9}],
        summary="Summary"
    )
    mock_recommender_class.return_value = mock_instance
    
    payload = {
        "city": "Delhi",
        "budget": "Low",
        "cuisines": ["Italian"],
        "min_rating": 4.0
    }
    
    response = client.post("/api/v1/recommend", json=payload)
    if response.status_code != 200:
        print(f"DEBUG Error: {response.json()}")
    assert response.status_code == 200
    assert response.json()["summary"] == "Summary"
