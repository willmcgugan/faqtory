# FAQtory

FAQtory is a tool to auto-generate a [FAQ.md](./FAQ.md) (Frequently Asked Questions) document for your project.

Additionally, a "suggest" feature uses fuzzy matching to reply to GitHub issues with suggestions from your FAQ.

## Getting started

Faqtory is best installed via [pipx](https://github.com/pypa/pipx) to avoid any dependency conflicts:

```bash
pipx install faqtory
```

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
  - "What does FAQ mean?"
---

FAQ stands for *Frequently Asked Questions*
```

The filename is unimportant, but a `title` is mandatory. You can also optionally add alternative titles under `alt_titles` which will be used with the `faqtory suggest` feature (but not displayed).

## Building

Run the following command to build the FAQ:

```bash
faqtory build
```

With the default settings this will generate an [FAQ.md](./FAQ.md) file.


## Suggest

The "suggest" subcommand can compile a list of FAQ entries that match a supplied issue title. Here's an example:

```bash
faqtory suggest "who is the author of FAQtory?"
```

This will generate a list of matching entries from the FAQ, and write Markdown to stdout. You can modify the output with the "suggest.md" template, which you will find in your ".faq/" directory (if you haven't configured it elsewhere),

This feature is designed to be used with a GitHub action to post an automated response. To enable this feature, copy [new_issue.yml](https://github.com/willmcgugan/faqtory/blob/main/.github/workflows/new_issue.yml) to a similarly named directory in your repository.


## Disclaimer

This was a hastily put together tool by a maintainer that was tired of responding to the same old issues. I can't devote much time to this project, but I will happily accept PRs!
