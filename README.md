# FAQtory

This is a tool to auto-generate Frequently Asked Questions (FAQs) documents.

You can compile a [FAQ.md](./FAQ.md) from individual `.question.md` documents. By default this will create a GitHub flavoured Markdown document, but you can edit a template to produce whatever format you like.

## Getting started

Install `faqtory` from PyPI. I'm going to assume you know how to do this bit.

Run the following from the directory you wish to store the FAQ document. 

```bash
faqtory init
```

This will create the following files and directories:

- `faq.yml` A configuration file which you can edit.
- `./.faq` A directory which stores templates.
- `./questions` A directory containing question documents.

## Adding questions

To add questions create a file with the extension `.question.md` in the questions directory (`./questions` if you are using the defaults).

Question documents are Markdown with front-matter. Here's an example:

```yml
---
title: "What does FAQ stand for?"

---

FAQ stands for *Frequently Asked Questions*
```

The filename is unimportant, but a `title` is mandatory. The body of the question can include any Markdown.

## Building

Run the following command to build the FAQ:

```bash
faqtory build
```

With the default settings this will generate an [FAQ.md](./FAQ.md) file.

## Roadmap

FAQtory is a work in progress, and a few hours work. The ultimate goal is to build a GitHub action that suggests answers to an issue from the FAQ.
