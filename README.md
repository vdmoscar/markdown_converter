# Markdown to HTML converter

Hi! Thanks for taking a look at my first public repository.

This is a learning/side project where I am building a Markdown parser and renderer from scratch in Python. The goal is to understand parsing, object-oriented design, and transforming structured text into HTML.

## What works

Currently it converts a basic subset of Markdown into HTML:

- Headings
- Paragraphs
- Images

## Next on the list

I am filled with determination to add these features:


- Code blocks
- Lists
- More Markdown features

## Project structure

The converter internally follows this pipeline:

Markdown file → Parser → Elements → HTML renderer

## Usage
The converter can be used through the CLI with the following command:
```bash
python main.py markdown_input_file html_output_file
```
## Example

### input

```markdown
# Hello

This is a paragraph.

![alt text](https://link_to_image.com)
```

### output
```html
<h1>Hello</h1>
<p>This is a paragraph.</p>
<img alt="alt text" src="https://link_to_image.com">
```

Stay determined!
