from element import Element
from text import Text
class ListItem(Element):
    def __init__(self, item):
        self.item_children = [item]

    @staticmethod
    def parse(context):
        item = ListItem.strip_markdown_list_item(context.get_current_line_indent_free())
        context.current_index += 1
        return ListItem(Text.parse(item))

    @staticmethod
    def strip_markdown_list_item(item):
        return item[2:].strip()

    def render_html(self):
        html = "<li>"
        for item in self.item_children:
                html += item.render_html()
        html += "</li>"
        return html

    def add_child(self, context):
        element = context.identify_current_line()
        self.item_children.append(element.parse(context))
