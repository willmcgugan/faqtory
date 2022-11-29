from __future__ import annotations


from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_faq(templates_path: str, **template_args) -> str:
    """Render FAQ.md"""
    env = Environment(
        loader=FileSystemLoader(templates_path), autoescape=select_autoescape()
    )

    template = env.get_template("FAQ.md")
    result = template.render(**template_args)
    return result


def render_suggest(templates_path: str, **template_args) -> str:
    """Render suggest.md"""
    env = Environment(
        loader=FileSystemLoader(templates_path), autoescape=select_autoescape()
    )

    template = env.get_template("suggest.md")
    result = template.render(**template_args)
    return result
