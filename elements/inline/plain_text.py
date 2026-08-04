from element import Element


class PlainText(Element):
    def __init__(self, content):
        self.content = content

    def parse(inline_context):
        content = inline_context.get_first_char()
        inline_context.current_index += 1
        while inline_context.identify_current_inline_element() == PlainText:
            content += inline_context.get_first_char()
            inline_context.current_index += 1

        return PlainText(content)

    def render_html(self):
        return self.content
