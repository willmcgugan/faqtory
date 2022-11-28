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
