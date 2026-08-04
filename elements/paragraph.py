from element import Element
from text import Text


class Paragraph(Element):
    def __init__(self, text: Text):
        self.text = text

    @staticmethod
    def parse(context):
        line = context.get_current_line()
        text = line
        while context.identify_next_line() == Paragraph:
            context.current_index += 1
            line = context.get_current_line()
            text += line
        context.current_index += 1
        text = text.strip()
        return Paragraph(Text.parse(text))

    def render_html(self):
        return f"<p>{self.text.render_html()}</p>"
