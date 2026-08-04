from element import Element
import re

class Bold(Element):
    regex = r"^\*\*(.*?)\*\*"
    def __init__(self, content):
        self.content = content

    @staticmethod
    def parse(inline_context):
        line = inline_context.get_line_from_current_index()
        match_object = re.match(Bold.regex, line)
        content = match_object.group(1)
        inline_context.current_index += match_object.end()
        return Bold(content)

    def render_html(self):
        return f"<strong>{self.content}</strong>"
