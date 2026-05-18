# Phase 0 Scope: AI-Powered Restaurant Recommendation System

This document defines the scope, stack, and boundaries for Milestone 1.

## Product Slice (v1)
The primary goal of Milestone 1 is to deliver a functional end-to-end recommendation flow:
- **Input**: User preferences via a basic web UI (primary) or developer CLI (diagnostics).
- **Process**: Retrieval from a static Zomato dataset filtered by location/cuisine, followed by LLM-based ranking and explanation.
- **Output**: A list of recommended restaurants with AI-generated justifications displayed in the web UI.

## Technical Stack
- **Language**: Python 3.9+
- **Backend Framework**: FastAPI
- **Frontend Framework**: React + Vite (SPA)
- **Data Source**: Hugging Face Datasets (`ManikaSaini/zomato-restaurant-recommendation`)
- **LLM Provider**: Groq (Llama-3 models)
- **Deployment**: Render (Backend) + Vercel (Frontend)

## Supported Preference Fields
1. **Location**: City-based filtering (e.g., New Delhi, Bangalore).
2. **Budget**: Categorical bands (Low, Medium, High).
3. **Cuisine**: Multi-select or text-based overlap.
4. **Minimum Rating**: Numeric threshold.
5. **Additional Context**: Free-text for custom needs (e.g., "outdoor seating", "romantic").

## Non-Goals (Out of Scope for Milestone 1)
- User Authentication and persistent profiles.
- Live Zomato API integration (static dataset only).
- Google Maps / Location-based auto-detection.
- Real-time table booking or ordering.
- Image uploads or social features.
