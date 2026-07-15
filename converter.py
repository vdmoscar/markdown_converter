class Converter:
    def __init__(self, file):
        self.file = file

    def toHTML(self):
        with open(self.file, "r") as md_file:
            for line in md_file.readlines():
                if line.startswith("#"):
                    line.replace("#")



converter = Converter("test.md")
converter.toHTML()