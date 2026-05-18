import click
from milestone1.phase0.commands import info, doctor
from milestone1.phase1.commands import ingest_smoke
from milestone1.phase2.commands import prefs_parse
from milestone1.phase3.commands import prompt_build
from milestone1.phase4.commands import recommend
from milestone1.phase5_api.commands import serve

@click.group()
def main():
    """Zomato AI Restaurant Recommendation System CLI."""
    pass

# Register commands
main.add_command(info)
main.add_command(doctor)
main.add_command(ingest_smoke)
main.add_command(prefs_parse)
main.add_command(prompt_build)
main.add_command(recommend)
main.add_command(serve)

if __name__ == "__main__":
    main()
