import click
import json
from milestone1.phase1.ingestor import load_restaurants
from milestone1.phase2.validator import preferences_from_mapping
from .service import filter_restaurants
from .prompt_builder import build_prompt_payload

@click.command(name="prompt-build")
@click.option("--city", required=True, help="Target city.")
@click.option("--budget", required=True, type=click.Choice(["Low", "Medium", "High"], case_sensitive=False), help="Budget band.")
@click.option("--cuisines", help="Comma-separated cuisines.")
@click.option("--rating", type=float, default=0.0, help="Min rating.")
@click.option("--context", help="Additional context.")
@click.option("--limit", type=int, default=15, help="Max candidates for LLM.")
def prompt_build(city, budget, cuisines, rating, context, limit):
    """Integrate data, filter results, and build the LLM prompt."""
    click.echo("Building integration layer output...")
    
    # 1. Load Data
    try:
        restaurants = load_restaurants(limit=None) # Load all for filtering
    except Exception as e:
        click.secho(f"Data Load Error: {e}", fg="red")
        return
        
    # 2. Parse Preferences
    data = {
        "city": city,
        "budget": budget,
        "cuisines": cuisines,
        "min_rating": rating,
        "additional_context": context
    }
    prefs, errors = preferences_from_mapping(data)
    if errors:
        click.secho("Preference Error:", fg="red", bold=True)
        for f, m in errors.items(): click.echo(f"  {f}: {m}")
        return
        
    # 3. Filter
    candidates = filter_restaurants(restaurants, prefs, limit=limit)
    click.echo(f"Filtered to {len(candidates)} candidates.")
    
    # 4. Build Prompt
    payload = build_prompt_payload(prefs, candidates)
    
    # 5. Output
    click.secho("\n--- PROMPT PAYLOAD ---", fg="cyan", bold=True)
    click.secho("\n[SYSTEM MESSAGE]", fg="yellow")
    click.echo(payload["system"])
    click.secho("\n[USER MESSAGE]", fg="yellow")
    click.echo(payload["user"])
    
    if not candidates:
        click.secho("\nWARNING: No candidates matched the filters. The LLM will be informed of an empty set.", fg="red", bold=True)
