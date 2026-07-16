from element import Element

class Paragraph(Element):
    def __init__(self, text):
        self.text = text

    @staticmethod
    def parse(context):
        line = context.get_current_line()
        text = line
        while context.identify_next_line() == Paragraph:
            context.current_index += 1
            line = context.get_current_line()
            text += line

        text = text.strip()
        return Paragraph(text)

    def render_html(self):
        pass