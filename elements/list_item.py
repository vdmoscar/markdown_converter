from element import Element

class ListItem(Element):
    def __init__(self, item):
        self.item = item
    
    @staticmethod
    def parse(context):
        if context.level < context.get_current_line_level():
            context.level = context.get_current_line_level()
            item = context.identify_current_line().parse(context)
        else:
            item = ListItem.strip_markdown_list_item(context.get_current_line())
        context.current_index += 1
        return ListItem(item)
    
    @staticmethod
    def strip_markdown_list_item(item):
        return item[2:].strip()
    
    def render_html(self):
        if type(self.item) == str:
            return f"<li>{self.item}</li>"
        return f"<li>{self.item.render_html()}</li>"
        
        
    