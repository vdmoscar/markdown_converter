from elements.heading import Heading
from elements.paragraph import Paragraph
from parse_context import ParseContext
import re
class Parser:
    element_list = [Heading]
    def __init__(self, lines):
        self.lines = lines
        self.document_list = []

    def parse(self):
        context = ParseContext(self.lines, self.element_list)
        while context.current_index < len(context.lines):
            element = context.identify_current_line()
            self.document_list.append(element.parse(context))
        return self.document_list