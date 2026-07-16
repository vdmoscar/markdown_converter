# Markdown to HTML converter

Hi! Thanks for taking a look at my first public repository.

This is a learning/side project where I am building a Markdown parser and renderer from scratch in Python. The goal is to understand parsing, object-oriented design, and transforming structured text into HTML.

## What works

Currently it converts a basic subset of Markdown into HTML:

- Headings
- Paragraphs

## Next on the list

I am filled with determination to add these features:

- Image conversion
- Code blocks
- Lists
- More Markdown features

## Project structure

The converter currently follows this pipeline:

Markdown file → Parser → Elements → HTML renderer


## Example

### input

```markdown
# Hello

This is a paragraph.
```

### output
```html
<h1>Hello</h1>
<p>This is a paragraph.</p>
```

Stay determined!
