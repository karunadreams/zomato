import click
import json
from milestone1.phase1.ingestor import load_restaurants
from milestone1.phase2.validator import preferences_from_mapping
from milestone1.phase3 import filter_restaurants, build_prompt_payload
from .client import GroqRecommender

@click.command(name="recommend")
@click.option("--city", required=True, help="Target city.")
@click.option("--budget", required=True, type=click.Choice(["Low", "Medium", "High"], case_sensitive=False), help="Budget band.")
@click.option("--cuisines", help="Comma-separated cuisines.")
@click.option("--rating", type=float, default=0.0, help="Min rating.")
@click.option("--context", help="Additional context.")
@click.option("--limit", type=int, default=15, help="Max candidates for LLM.")
@click.option("--count", type=int, default=5, help="Number of top recommendations to return.")
def recommend(city, budget, cuisines, rating, context, limit, count):
    """End-to-end restaurant recommendation using Groq LLM."""
    click.echo("[INFO] Starting recommendation engine...")
    
    # 1. Integration Layer (Phase 1-3)
    try:
        restaurants = load_restaurants(limit=None)
        
        data = {
            "city": city,
            "budget": budget,
            "cuisines": cuisines,
            "min_rating": rating,
            "additional_context": context
        }
        prefs, errors = preferences_from_mapping(data)
        if errors:
            click.secho(f"Preference Error: {errors}", fg="red")
            return
            
        candidates = filter_restaurants(restaurants, prefs, limit=limit)
        if not candidates:
            click.secho("No candidates found matching your filters. Try broadening your search.", fg="yellow")
            return
            
        payload = build_prompt_payload(prefs, candidates, top_n=count)
    except Exception as e:
        click.secho(f"Initialization Error: {e}", fg="red")
        return

    # 2. LLM Layer (Phase 4)
    click.echo(f"Sending {len(candidates)} candidates to Groq AI...")
    try:
        recommender = GroqRecommender()
        response = recommender.recommend(payload)
    except Exception as e:
        click.secho(f"LLM Error: {e}", fg="red")
        return

    # 3. Output
    click.secho("\n--- AI RECOMMENDATIONS ---", fg="green", bold=True)
    
    for i, rec in enumerate(response.recommendations, 1):
        click.echo(f"{i}. {click.style(rec.name, bold=True)}")
        click.echo(f"   Match Score: {int(rec.score * 100)}%")
        click.echo(f"   Reasoning: {rec.reasoning}")
        click.echo("-" * 40)
