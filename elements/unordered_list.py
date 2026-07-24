from element import Element
from elements.list_item import ListItem

class UnorderedList(Element):
    regex = r"-\s.*"

    def __init__(self, list_items: list):
        self.list_items = list_items
    
    @staticmethod
    def parse(context):
        list_items = [ListItem.parse(context)]
        while context.identify_next_line() == UnorderedList:
            context.current_index += 1
            list_items.append(ListItem.parse(context))
        return UnorderedList(list_items)
    
    def render_html(self):
        html = "<ul>\n"
        for item in self.list_items:
            html += f"{item.render_html()}\n"
        html += "</ul>"
        return html
    
    
        