from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import Question


class Questions:
    def __init__(self) -> None:

        self.questions: list[Question] = []

    def read_all(self, path) -> None:
        for question_path in Path(path).glob("*.question.md"):
            question = Question.read(question_path)
            self.questions.append(question)

    def build(self, templates_path: str) -> str:

        env = Environment(
            loader=FileSystemLoader(templates_path), autoescape=select_autoescape()
        )

        questions = sorted(self.questions, key=lambda question: question.title.lower())

        template = env.get_template("FAQ.md")
        faq = template.render(questions=questions)
        return faq
