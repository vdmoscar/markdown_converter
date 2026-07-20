from element import Element

class UnorderedList(Element):
    regex = r"-\s.*"

    def __init__(self, list_items: list):
        self.list_items = list_items
    
    @staticmethod
    def parse(context):
        list_items = [UnorderedList.strip_markdown_list_item(context.get_current_line())]
        while context.identify_next_line() == UnorderedList:
            context.current_index += 1
            list_items.append(UnorderedList.strip_markdown_list_item(context.get_current_line()))
        context.current_index += 1
        return UnorderedList(list_items)
    
    @staticmethod
    def strip_markdown_list_item(item):
        return item[2:].strip()
    
    def render_html(self):
        html = "<ul>\n"
        for item in self.list_items:
            html += f"<li>{item}</li>\n"
        html += "</ul>"
        return html
    
    
        