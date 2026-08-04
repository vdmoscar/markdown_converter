from element import Element
from text import Text
import re


class Image(Element):
    regex = r"!\[([^\]]*)\]\(([^)]*)\)"

    def __init__(self, text, url):
        self.text = text
        self.url = url

    @staticmethod
    def parse(context):
        match = re.match(Image.regex, context.get_current_line_indent_free())
        text = match.group(1)
        url = match.group(2)
        context.current_index += 1
        return Image(Text.parse(text), url)

    def render_html(self):
        return f"<img alt='{self.text.render_html()}' src='{self.url}'>"
