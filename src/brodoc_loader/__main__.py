from typer import Typer

cli = Typer()

@cli.command()
def hello():
    print("Hello.")

@cli.command()
def bye(name: str):
    print(f"Bye {name}")

if __name__ == "__main__":
    cli()