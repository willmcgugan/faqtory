from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown

from .models import Config
from .questions import Questions

import click
from importlib.metadata import version

CONFIG_PATH = "./faq.yml"
QUESTIONS_PATH = "./questions"
TEMPLATES_PATH = ".faq"
FAQ_PATH = "./FAQ.md"


QUESTIONS_README = """
# Questions

Your questions should go in this directory.

Question files should be named with the extension ".question.md".

"""

FAQ_TEMPLATE = """
# Frequently Asked Questions 

{%- for question in questions %}
<details>  
  <summary><b>{{ question.title }}</b></summary>
  <p>

  {{ question. body }}
</details>
{% endfor %}

"""


@click.group()
@click.version_option(version("faq"))
def run():
    pass


@run.command()
@click.option(
    "--config", help="Path to config file", default=CONFIG_PATH, metavar="PATH"
)
@click.option(
    "--questions", help="Path to questions", default=QUESTIONS_PATH, metavar="PATH"
)
@click.option(
    "--templates", help="Path to templates", default=TEMPLATES_PATH, metavar="PATH"
)
@click.option(
    "--output", help="Path to generated FAQ", default=FAQ_PATH, metavar="PATH"
)
@click.option(
    "--overwrite/-no-overwrite",
    help="Overwrite files if they exist",
    default=False,
)
def init(
    config: str, questions: str, templates: str, output: str, overwrite: bool
) -> None:
    console = Console()
    error_console = Console(stderr=True)

    DEFAULT_CONFIG = f"""\
# FAQ configuration
questions_path: "{questions}"
output_path: "{output}"
templates_path: "{templates}"\
"""

    def write_path(path: Path, text: str) -> bool:
        try:
            with path.open("w" if overwrite else "x") as write_file:
                write_file.write(text)
        except FileExistsError:
            error_console.print(
                f"[red]⚠[/] File {str(path)!r} exists, use [b]--overwrite[/b] to update"
            )
            return False
        except Exception as error:
            error_console.print(f"[red]⚠[/] Unable to write {path}; {error}")
            return False

        console.print(f"[green]✔[/] Wrote {str(path)!r}")
        return True

    def make_directory(path: Path) -> bool:
        try:
            path.mkdir(parents=True, exist_ok=True)
        except Exception as error:
            error_console.print(f"unable to create {str(path)!r} directory; {error}")
            return False
        console.print(f"[green]✔[/] Directory {str(path)!r} created (or exists)")
        return True

    if write_path(Path(config), DEFAULT_CONFIG):
        console.print(
            Panel(
                Syntax(DEFAULT_CONFIG, "yaml", line_numbers=True),
                title=config,
            ),
        )

    make_directory(Path(questions))
    make_directory(Path(templates))

    readme_path = Path(questions) / "README.md"
    write_path(readme_path, QUESTIONS_README)
    write_path(Path(templates) / "FAQ.md", FAQ_TEMPLATE)


@run.command()
@click.option(
    "--config", help="Path to config file", default=CONFIG_PATH, metavar="PATH"
)
@click.option(
    "--echo/-no-echo",
    help="Write generated file to terminal",
    default=False,
)
def build(config: str, echo: bool) -> None:
    console = Console()
    config_data = Config.read(Path(config))
    questions = Questions()

    questions.read_all(config_data.questions_path)
    faq = questions.build(config_data.templates_path)

    if echo:
        console.print(Syntax(faq, "markdown"))

    Path(config_data.output_path).write_text(faq)
