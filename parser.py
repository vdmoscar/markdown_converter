from elements.heading import Heading
from elements.image import Image
from elements.unordered_list import UnorderedList
from parse_context import ParseContext


class Parser:
    element_list = [Heading, Image, UnorderedList]
    def __init__(self, lines):
        self.lines = lines
        self.document_list = []

    def parse(self):
        context = ParseContext(self.lines, self.element_list)
        while context.current_index < len(context.lines):
            element = context.identify_current_line()
            self.document_list.append(element.parse(context))
        return self.document_list