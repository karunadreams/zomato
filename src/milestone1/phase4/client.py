import os
import json
import logging
from typing import Dict, Optional
from groq import Groq
from dotenv import load_dotenv
from .models import RecommendationResponse

load_dotenv()

logger = logging.getLogger(__name__)

class GroqRecommender:
    def __init__(self, api_key: Optional[str] = None, model: str = "llama-3.3-70b-versatile"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY must be provided in .env or as an argument.")
        
        self.client = Groq(api_key=self.api_key)
        self.model = os.getenv("GROQ_MODEL", model)

    def recommend(self, payload: Dict) -> RecommendationResponse:
        """
        Send the prompt payload to Groq and parse the JSON response.
        """
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": payload["system"]},
                    {"role": "user", "content": payload["user"]},
                ],
                model=self.model,
                response_format={"type": "json_object"},
                temperature=0.1, # Keep it deterministic
            )
            
            content = chat_completion.choices[0].message.content
            if not content:
                raise ValueError("Empty response from Groq API")
                
            data = json.loads(content)
            return RecommendationResponse(**data)
            
        except Exception as e:
            logger.error(f"Groq API Error: {e}")
            raise
