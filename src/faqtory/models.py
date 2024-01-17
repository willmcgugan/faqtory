from __future__ import annotations

import string
from pathlib import Path
from typing import List


from thefuzz import fuzz
import frontmatter
from yaml import load, Loader


from pydantic import BaseModel


class Question(BaseModel):
    title: str
    body: str
    alt_titles: List[str] = []

    @property
    def slug(self) -> str:
        """Create a slug from the title.

        Returns:
            str: Slug suitable for use in an anchor.
        """
        chars_to_remove = string.punctuation
        chars_to_remove = chars_to_remove.replace("-", "").replace("_", "")
        slug = self.title.lower()
        slug = slug.translate(str.maketrans("", "", chars_to_remove))
        slug = slug.replace(" ", "-")
        return slug

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
            alt_titles=metadata.get("alt_titles", []),
        )
        return question

    @property
    def titles(self) -> list[str]:
        """Get all titles including alternatives"""
        return [self.title, *self.alt_titles]

    def match(self, query: str) -> int:
        """Match this question against a query"""
        return max(fuzz.partial_ratio(query, title) for title in self.titles)


class Config(BaseModel):
    questions_path: str
    output_path: str
    templates_path: str
    faq_url: str

    @classmethod
    def read(cls, path: Path) -> "Config":
        with open(path, "rb") as config_file:
            config_data = load(config_file, Loader=Loader)

        def get_str(key: str) -> str:
            return config_data.get(key, "")

        config = cls(
            questions_path=get_str("questions_path"),
            output_path=get_str("output_path"),
            templates_path=get_str("templates_path"),
            faq_url=get_str("faq_url"),
        )
        return config
