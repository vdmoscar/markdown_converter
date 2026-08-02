from element import Element
import re

class Strikethrough(Element):
    regex = r"^~~(.*?)~~"
    def __init__(self, content):
        self.content = content

    def parse(inline_context):
        line = inline_context.get_line_from_current_index()
        match_object = re.match(Strikethrough.regex, line)
        content = match_object.group(1)
        inline_context.current_index += len(match_object.group(1)) + 4
        return Strikethrough(content)

    def render_html(self):
        return f"<del>{self.content}</del>"
