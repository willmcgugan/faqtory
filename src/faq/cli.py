from rich.console import Console

import click
from importlib.metadata import version


@click.group()
@click.version_option(version("faq"))
def run():
    pass
