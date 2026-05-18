import click
import uvicorn

@click.command(name="serve")
@click.option("--host", default="127.0.0.1", help="Host to bind.")
@click.option("--port", default=8000, help="Port to bind.")
@click.option("--reload", is_flag=True, help="Enable auto-reload.")
def serve(host, port, reload):
    """Start the FastAPI backend server."""
    click.secho(f"Starting API server on http://{host}:{port}", fg="green", bold=True)
    uvicorn.run("milestone1.phase5_api.app:app", host=host, port=port, reload=reload)
