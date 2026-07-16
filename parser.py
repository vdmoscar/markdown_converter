from elements.heading import Heading
from elements.paragraph import Paragraph
import re
class Parser:
    element_list = [Heading]
    def __init__(self, md_input):
        self.md_input = md_input

    def parse(self):
        # should return a list of element objects
        pass

    @staticmethod
    def identify_line(line):
        for element in Parser.element_list:
            if element.regex and re.match(element.regex, line):
                return element
        return Paragraph

