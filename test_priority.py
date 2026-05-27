import click
from click.core import ParameterSource

@click.command()
@click.option("--name", envvar="APP_NAME", default="guest", prompt=True)
@click.pass_context
def cli(ctx, name):
    source = ctx.get_parameter_source("name")
    click.echo(f"name: {name}, source: {source}")

if __name__ == "__main__":
    cli(default_map={"name": "carol"})