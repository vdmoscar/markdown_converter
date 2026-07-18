from element import Element
import re

class Image(Element):
    regex = r"!\[([^\]]*)\]\(([^)]*)\)"

    def __init__(self, text, url):
        self.text = text
        self.url = url
        
    
    @staticmethod
    def parse(context):
        match = re.match(Image.regex, context.get_current_line())
        text = match.group(1)
        url = match.group(2)
        context.current_index += 1
        return Image(text, url)
    
    def render_html(self):
        return f"<img src='{self.url}' alt='{self.text}'>\n"



        


