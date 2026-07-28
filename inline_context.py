from elements.inline.plain_text import PlainText
import re

class InlineContext:
    def __init__(self, line, element_list, index):
        self.line = line
        self.element_list = element_list
        self.current_index = index

    def get_line_from_index(self, index):
        return self.line[index:]

    def get_line_from_current_index(self):
        if self.current_index < len(self.line):
            return self.get_line_from_index(self.current_index)
        return None

    def identify_inline_element(self, line):
        for element in self.element_list:
            if element.regex and re.match(element.regex, line):
                return element
        return PlainText

    def identify_current_inline_element(self):
        line = self.get_line_from_current_index()
        if line:
            return self.identify_inline_element(line)
        return None


    def get_first_char(self):
        try:
            return self.get_line_from_current_index()[0]
        except IndexError:
            return None

