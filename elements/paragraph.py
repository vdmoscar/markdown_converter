from element import Element

class Paragraph(Element):
    def __init__(self, text):
        self.text = text

#    @staticmethod
#    def parse(index, file):
#        line = file[index]
#        text = line
#        index += 1
#        while Parser.identify_line(file[index]) == Paragraph:
#            line = file[index]
#            text += line
#            index += 1
#        text = text.strip()
#        return index, Paragraph(text)