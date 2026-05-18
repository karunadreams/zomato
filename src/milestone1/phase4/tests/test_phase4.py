import pytest
from unittest.mock import MagicMock, patch
from ..client import GroqRecommender
from ..models import RecommendationResponse

@pytest.fixture
def mock_payload():
    return {
        "system": "Persona",
        "user": "Data"
    }

def test_groq_recommender_parsing(mock_payload):
    # Mock response from Groq
    mock_content = {
        "recommendations": [
            {"name": "Test Resto", "reasoning": "Good food", "score": 0.9}
        ],
        "summary": "Summary here"
    }
    
    with patch("milestone1.phase4.client.Groq") as MockGroq:
        mock_client = MagicMock()
        MockGroq.return_value = mock_client
        
        # Mock the chat completion response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = '{"recommendations": [{"name": "Test Resto", "reasoning": "Good food", "score": 0.9}], "summary": "Summary here"}'
        mock_client.chat.completions.create.return_value = mock_response
        
        recommender = GroqRecommender(api_key="test-key")
        result = recommender.recommend(mock_payload)
        
        assert isinstance(result, RecommendationResponse)
        assert result.recommendations[0].name == "Test Resto"
        assert result.summary == "Summary here"

def test_groq_recommender_missing_api_key():
    with patch.dict("os.environ", {"GROQ_API_KEY": ""}):
        with pytest.raises(ValueError, match="GROQ_API_KEY must be provided"):
            GroqRecommender(api_key=None)
