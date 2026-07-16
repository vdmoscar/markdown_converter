from parser import Parser
from render import Renderer

input_file = "tests/test_heading.md"
output_file = "test.html"

parser = Parser(input_file)
parser.parse()
renderer = Renderer(parser.document_list, output_file)
renderer.render()