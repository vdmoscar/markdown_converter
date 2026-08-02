from elements.inline.italic import Italic
from elements.inline.bold import Bold
from elements.inline.strikethrough import Strikethrough
from inline_context import InlineContext

class Text:
    text_elements = [Bold, Italic, Strikethrough]
    def __init__(self, text_items):
        self.text_items = text_items

    def parse(line):
        text = []
        inline_context = InlineContext(line, Text.text_elements, 0)
        while inline_context.current_index < len(line):
            inline_element = inline_context.identify_current_inline_element()
            text.append(inline_element.parse(inline_context))

        return Text(text)

    def render_html(self):
        html = ""
        for item in self.text_items:
            html += item.render_html()
        return html
