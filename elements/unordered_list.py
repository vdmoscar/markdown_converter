from element import Element
from elements.list_item import ListItem

class UnorderedList(Element):
    regex = r"-\s.*"

    def __init__(self, list_items: list):
        self.list_items = list_items

    @staticmethod
    def parse(context):
        list_items = [ListItem.parse(context)]
        while context.has_next_line():
            if UnorderedList.current_line_is_child(context):
                old_level = context.level
                context.level = context.get_current_line_level()
                list_items[-1].add_child(context)
                context.level = old_level

            elif UnorderedList.current_line_is_a_sibling(context):
                element = context.identify_current_line()
                if element == UnorderedList:
                    list_items.append(ListItem.parse(context))
                else:
                    list_items[-1].add_child(context)

            else:
                return UnorderedList(list_items)

        return UnorderedList(list_items)

    @staticmethod
    def current_line_is_a_sibling(context):
        return (context.level > 0 and context.level == context.get_current_line_level()) or (context.level == 0 and context.identify_current_line() == UnorderedList)

    @staticmethod
    def current_line_is_child(context):
        return context.get_current_line_level() > context.level

    def render_html(self):
        html = "<ul>\n"
        for item in self.list_items:
            html += f"{item.render_html()}\n"
        html += "</ul>"
        return html


