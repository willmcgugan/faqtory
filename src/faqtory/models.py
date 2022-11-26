from dataclasses import dataclass
from pathlib import Path

import frontmatter
from yaml import load, Loader


@dataclass
class Question:
    title: str
    body: str

    @property
    def slug(self) -> str:
        return self.title.lower().replace(" ", "-").replace("?", "")

    @classmethod
    def read(cls, path: Path) -> "Question":
        """Read a question (Markdown with frontmatter)

        Args:
            path (str): Path to markdown.

        Returns:
            Question: A Question object
        """
        question_data = frontmatter.load(path)
        content = question_data.content
        metadata = question_data.metadata
        question = cls(
            title=metadata.get("title", ""),
            body=content,
        )
        return question


@dataclass
class Config:
    questions_path: str
    output_path: str
    templates_path: str

    @classmethod
    def read(cls, path: Path) -> "Config":
        with open(path, "rb") as config_file:
            config_data = load(config_file, Loader=Loader)

        def get_str(key: str) -> str:
            return config_data[key]

        config = cls(
            questions_path=get_str("questions_path"),
            output_path=get_str("output_path"),
            templates_path=get_str("templates_path"),
        )
        return config
