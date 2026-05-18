import click
from .ingestor import load_restaurants

@click.command(name="ingest-smoke")
@click.option("--limit", default=5, help="Number of restaurants to show.")
def ingest_smoke(limit):
    """Smoke test for data ingestion: fetch and display N restaurants."""
    click.echo(f"Running ingestion smoke test (limit={limit})...")
    
    try:
        restaurants = load_restaurants(limit=limit)
        
        if not restaurants:
            click.secho("No restaurants found.", fg="yellow")
            return
            
        click.secho(f"\nSuccessfully loaded {len(restaurants)} restaurants:\n", fg="green", bold=True)
        
        for i, res in enumerate(restaurants, 1):
            # Use safe strings for Windows terminal
            name = res.name.encode('ascii', 'ignore').decode('ascii')
            city = res.city.encode('ascii', 'ignore').decode('ascii')
            cuisines = ", ".join(res.cuisines).encode('ascii', 'ignore').decode('ascii')
            
            click.echo(f"{i}. {name} ({city})")
            click.echo(f"   Cuisines: {cuisines}")
            click.echo(f"   Cost: Rs. {res.cost_for_two} | Rating: {res.rating} ({res.votes} votes) | Band: {res.budget_band}")
            click.echo("-" * 40)
            
    except Exception as e:
        click.secho(f"Error during ingestion: {e}", fg="red")
