# Devlog for the converter

## The idea

The converter should be able to create static html pages out of markdown files. The goal of this is to automate a blog concept for the website. So that i can add my markdown files to it which get turned into the right htlml files for the webpage


### steps:

1. You have the markdown file
2. the markdown file gets parsed into the right headings
3. the parsed information gets then rendered into html
4. automated push to the server

### step 2

the file should be turned into a list of objects. like every element should have it's class.

list of basic elements:
- paragraph (just text)
- heading (text and a level)
- list (ul and ol, unorderd and orderd, could be a variable)

list of extra elements:
- images (link, alt/caption)
- code blocks (text, which code block)

list of things to check inside the text of each element:
- link
- nested list
- image??? this could be rare but arround the same structure as a link



it could be an idea to also make things like italic and bold possible but this could be something for later.



#### example

# Hi this is a test number 1

- test 1
- test 2
just a normal test

=> [Heading(level1, "Hi this is a test number 1"), List(unorderd, "test 1", "test 2"), Paragraph("just a normal test)]

The text property of each element should make it's own structure like this:

"Hi this is a *special* test with a link to be a [big shot](https://www.youtube.com/watch?v=V31PVkwzpEY)"
=> [text("Hi this is a special"), Italic("special), text("test with a link to be a ), Link("big shot", "https://www.youtube.com/watch?v=V31PVkwzpEY")]

### Step 3

the list of element objects should be rendered into a html static page. This should not be the hardest part because once everything parses correctly this is just writing the right f strings tbh.



## Some design questions:

How do we detect nested lists?

this could be solved by counting the identation with lists. Or/and lists could be seen as an inline item of text
