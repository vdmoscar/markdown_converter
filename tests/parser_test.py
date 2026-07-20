import pytest
from elements.heading import Heading
from elements.paragraph import Paragraph
from elements.image import Image
from elements.unordered_list import UnorderedList
from parser import Parser
from parse_context import ParseContext

ELEMENT_LIST = [Heading, Image, UnorderedList]

def test_parseContext_identify_heading():
    parse_context = ParseContext("empty", ELEMENT_LIST, 1)
    test1 = "# heading"
    test2 = "##### heading"
    test3 = "not ### a heading"
    test4 = "#not a heading"
    assert parse_context.identify_line(test1) == Heading
    assert parse_context.identify_line(test2) == Heading
    assert parse_context.identify_line(test3) == Paragraph
    assert parse_context.identify_line(test4) == Paragraph

def test_parse_heading():
    with open("tests/test_heading.md", "r") as file:
        test_lines = file.readlines()
        context = ParseContext(test_lines, ELEMENT_LIST, 0)
        heading_1 = Heading.parse(context)
        assert heading_1.level == 1
        assert heading_1.text == "test"
        assert context.current_index == 1
        context.current_index = 8
        heading_2 = Heading.parse(context)
        assert heading_2.level == 3
        assert heading_2.text == "second test but it has 3 levels huh"
        assert context.current_index == 9

def test_parse_paragraph():
    with open("tests/test_paragraph.md", "r") as file:
        test_lines  = file.readlines()
        context = ParseContext(test_lines, ELEMENT_LIST, 2)

        paragraph_1 = Paragraph.parse(context)
        assert paragraph_1.text == "a one liner of a paragraph"
        assert context.current_index == 4

        context.current_index = 6
        paragraph_2 = Paragraph.parse(context)
        assert paragraph_2.text == "NOW IS YOUR CHANGE TO BE A BIG SHOT\nBE A BIG SHOT\nB B B B B BE A BIG SHOT"
        assert context.current_index == 9

def test_parse_image():
    with open("tests/test_image.md", "r") as file:
        test_lines = file.readlines()
        context = ParseContext(test_lines, ELEMENT_LIST, 1)

        assert context.identify_current_line() == Image

        test_image = Image.parse(context)
        assert test_image.url == "https://test.com"
        assert test_image.text == "it works"

def test_parse_unorderd_list():
    with open("tests/test_ul.md", "r") as file:
        test_lines = file.readlines()
        context = ParseContext(test_lines, ELEMENT_LIST, 0)

        assert context.identify_current_line() == UnorderedList
        test_list = UnorderedList.parse(context)
        assert len(test_list.list_items) == 2
        assert test_list.list_items[0] == "test"

def test_parse_nested_list():
    with open("tests/test_ul.md", "r") as file:
        test_lines = file.readlines()
        context = ParseContext(test_lines, ELEMENT_LIST, 4)

        assert context.get_line_level("\ttest the rage") == 1
        assert context.get_current_line_level() == 1
        assert context.get_next_line_level() == 2

def test_parser():
    with open("tests/test_heading.md", "r") as file:
        test = file.readlines()
        parser = Parser(test)
        parser.parse()
        assert len(parser.document_list) == 3