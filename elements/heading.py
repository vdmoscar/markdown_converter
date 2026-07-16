from element import Element

class Heading(Element):
    regex = r"^#{1,6}\s.*"
    def __init__(self, text, level):
        self.text = text
        self.level = level

    @staticmethod
    def parse(context):
        line = context.get_current_line()
        level = 0
        while line[level] == '#':
            level += 1
        text = line[level + 1:].strip()
        context.current_index += 1
        return Heading(text, level)

    def render_html(self):
        return f"<h{self.level}>{self.text}</h{self.level}>"