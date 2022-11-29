# FAQtory

This is a tool to auto-generate Frequently Asked Questions (FAQs) documents.

FAQtory compiles a [FAQ.md](./FAQ.md) from individual `.question.md` documents. By default this will create a GitHub flavoured Markdown document, but you can edit a template to produce whatever format you like.

## Getting started

Install `faqtory` from PyPI. I'm going to assume you know how to do this bit.

Run the following from the directory you wish to store the FAQ document. 

```bash
faqtory init
```

This will create the following files and directories:

- `faq.yml` A configuration file which you can edit.
- `./.faq/` A directory which will contain templates.
- `./questions/` A directory containing question documents.

## Adding questions

To add questions create a file with the extension `.question.md` in the questions directory (`./questions/` if you are using the defaults).

Question documents are Markdown with front-matter. Here's an example:

```yml
---
title: "What does FAQ stand for?"
alt_titles:
  - "What is the meaning of FAQ?"
---

FAQ stands for *Frequently Asked Questions*
```

The filename is unimportant, but a `title` is mandatory. You can also add alternative titles under `alt_titles` which will be used with the `faqtory suggest` feature (but not displayed),

## Building

Run the following command to build the FAQ:

```bash
faqtory build
```

With the default settings this will generate an [FAQ.md](./FAQ.md) file.


## Suggest

FAQtory can suggest an entry from the FAQ by matching a query against the question titles.

```bash
faqtory suggest "who is the author of FAQtory?"
```

This will generate a list of matching entries from the FAQ, and write Markdown to stdout. You can modify the output with the "suggest.md" template, which you will find in ".faq/" (if you haven't configured it elsewhere),

This feature is designed to be used with a GitHub action to post an automated response. To enable this feature on your repository, copy [new_issue.yml](https://github.com/willmcgugan/faqtory/blob/main/.github/workflows/new_issue.yml) to a similarly named directory.
