class Renderer:
    def __init__(self, document_list, output_file):
        self.document_list = document_list
        self.output_file = output_file

    def render(self):
        with open(self.output_file, "w") as file:
            for element in self.document_list:
                file.write(element.render_html())

