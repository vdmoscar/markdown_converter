from parser import Parser
from render import Renderer


def convert_to_html(markdown: list[str]):
    parser = Parser(markdown)
    document = parser.parse()
    renderer = Renderer(document)
    return renderer.render()