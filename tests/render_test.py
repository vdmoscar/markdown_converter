import pytest
from elements.heading import Heading
from elements.paragraph import Paragraph
from elements.image import Image
from render import Renderer


def test_render_heading():
    renderer = Renderer([Heading("test", 1)])
    assert renderer.render() == "<h1>test</h1>\n"

    renderer.document_list = [Heading(f"test{n}", n) for n in range(1, 7)]
    assert renderer.render() == "<h1>test1</h1>\n<h2>test2</h2>\n<h3>test3</h3>\n<h4>test4</h4>\n<h5>test5</h5>\n<h6>test6</h6>\n"


def test_render_paragraph():
    renderer = Renderer([Paragraph("test")])
    assert renderer.render() == "<p>test</p>\n"

def test_render_image():
    renderer = Renderer([Image("test", "https://test.com")])
    assert renderer.render() == "<img alt='test' src='https://test.com'>\n"