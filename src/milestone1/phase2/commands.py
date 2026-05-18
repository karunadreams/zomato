import click
import json
from .validator import preferences_from_mapping

@click.command(name="prefs-parse")
@click.option("--city", required=True, help="Target city (e.g. Bangalore)")
@click.option("--budget", required=True, type=click.Choice(["Low", "Medium", "High"], case_sensitive=False), help="Budget band.")
@click.option("--cuisines", help="Comma-separated cuisines (e.g. 'Italian, Chinese').")
@click.option("--rating", type=float, default=0.0, help="Minimum rating (0.0 - 5.0).")
@click.option("--context", help="Additional context/notes.")
def prefs_parse(city, budget, cuisines, rating, context):
    """Validate and parse user preferences."""
    data = {
        "city": city,
        "budget": budget,
        "cuisines": cuisines,
        "min_rating": rating,
        "additional_context": context
    }
    
    prefs, errors = preferences_from_mapping(data)
    
    if errors:
        click.secho("\nValidation Failed:", fg="red", bold=True)
        for field, msg in errors.items():
            click.echo(f"  - {field}: {msg}")
        return
    
    click.secho("\nPreferences Validated Successfully:", fg="green", bold=True)
    # Print as formatted JSON
    click.echo(json.dumps(prefs.dict(), indent=2))
