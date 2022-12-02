from __future__ import annotations


from pathlib import Path

from .models import Question


def read_questions(path: str) -> list[Question]:
    questions: list[Question] = []
    for question_path in Path(path).glob("*.question.md"):
        question = Question.read(question_path)
        questions.append(question)
    questions.sort(key=lambda question: question.title.lower())
    return questions
