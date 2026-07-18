class Renderer:
    def __init__(self, document_list):
        self.document_list = document_list

    def render(self):
        html = ""
        for element in self.document_list:
            html += f"{element.render_html()}\n"
        return html

