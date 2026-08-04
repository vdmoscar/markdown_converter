from element import Element
import re


class Link(Element):
    regex = r"\[([^\]]*)\]\(([^)]*)\)"

    def __init__(self, content, url):
        self.content = content
        self.url = url

    @staticmethod
    def parse(inline_context):
        line = inline_context.get_line_from_current_index()
        match_object = re.match(Link.regex, line)
        content = match_object.group(1)
        url = match_object.group(2)
        inline_context.current_index += match_object.end()
        return Link(content, url)

    def render_html(self):
        return f"<a href='{self.url}'>{self.content}</a>"
