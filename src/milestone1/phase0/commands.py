import os
import click
from milestone1 import __version__

@click.command()
def info():
    """Display project version and basic status."""
    click.echo(f"Zomato Recommendation System - Milestone 1")
    click.echo(f"Version: {__version__}")
    click.echo(f"Status: Phase 0 Initialized")

@click.command()
def doctor():
    """Check environment configuration and dependencies."""
    click.echo("Running system check...")
    
    # Check for .env file
    env_exists = os.path.exists(".env")
    if env_exists:
        click.secho("[OK] .env file found", fg="green")
    else:
        click.secho("[FAIL] .env file missing (see .env.example)", fg="red")
        
    # Check for GROQ_API_KEY
    from dotenv import load_dotenv
    load_dotenv()
    
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key and len(groq_key) > 10:
        click.secho("[OK] GROQ_API_KEY is set", fg="green")
    else:
        click.secho("[FAIL] GROQ_API_KEY is missing or invalid", fg="red")
        
    if env_exists and groq_key:
        click.secho("\nSystem is ready for development.", fg="cyan", bold=True)
    else:
        click.secho("\nPlease fix the issues above to proceed.", fg="yellow")
