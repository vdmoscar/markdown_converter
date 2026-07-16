from element import Element

class Heading(Element):
    regex = r"^#{1,6}\s.*"
    def __init__(self, text, level):
        self.text = text
        self.level = level

    @staticmethod
    def parse(index, file):
        line = file[index]
        level = 0
        while line[level] == '#':
            level += 1
        text = line[level + 1:].strip()
        return index + 1, Heading(text, level)

    def render_html(self):
        pass