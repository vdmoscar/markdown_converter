from elements.heading import Heading
from elements.paragraph import Paragraph
import re

class ParseContext:
    def __init__(self, lines, element_list, current_index = 0):
        self.lines = lines
        self.element_list = element_list
        self.current_index = current_index

    def identify_line(self, line):
        for element in self.element_list:
            if element.regex and re.match(element.regex, line):
                return element
        return Paragraph

    def get_next_line(self):
        if self.has_next_line():
            return self.lines[self.current_index + 1]
        return None

    def get_current_line(self):
        return self.lines[self.current_index]

    def identify_next_line(self):
        line = self.has_next_line()

        if line:
            return self.identify_line(self.get_next_line())

        return None

    def identify_current_line(self):
        return self.identify_line(self.get_current_line())

    def get_line_level(self, line: str):
        level = 0
        if line.startswith("\t"):
            for char in line:
                if char != "\t":
                    return level
                level += 1
        
        if line.startswith("    "):
            level += 1 + self.get_line_level(line[4:])
            
        return level
    
    def get_current_line_level(self):
        return self.get_line_level(self.get_current_line())
    
    def get_next_line_level(self):
        line = self.get_next_line()
        if line:
            return self.get_line_level(line)
        return None
    
    def has_next_line(self):
        return self.current_index + 1 < len(self.lines)