import pytest
from elements.heading import Heading
from elements.paragraph import Paragraph
from parser import Parser
from parse_context import ParseContext

ELEMENT_LIST = [Heading]

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

def test_parser():
    parser = Parser("tests/test_heading.md")
    parser.parse()
    assert len(parser.document_list) == 3