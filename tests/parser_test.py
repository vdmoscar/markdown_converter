import pytest
from elements.heading import Heading
from elements.paragraph import Paragraph
from parser import Parser

def test_identify_heading():
    test1 = "# heading"
    test2 = "##### heading"
    test3 = "not ### a heading"
    test4 = "#not a heading"
    assert Parser.identify_line(test1) == Heading
    assert Parser.identify_line(test2) == Heading
    assert Parser.identify_line(test3) == Paragraph
    assert Parser.identify_line(test4) == Paragraph

def test_parse_heading():
    with open("tests/test_heading.md", "r") as file:
        test = file.readlines()
        index1, heading_1 = Heading.parse(0, test)
        index2, heading_2 = Heading.parse(8, test)
        assert heading_1.level == 1
        assert heading_1.text == "test"
        assert index1 == 1
        assert heading_2.level == 3
        assert heading_2.text == "second test but it has 3 levels huh"
        assert index2 == 9

def test_parse_paragraph():
    with open("tests/test_paragraph", "r") as file:
        test  = file.readlines()
        index1, paragraph_1 = Paragraph.parse(2, test)
        index2, paragraph_2 = Paragraph.parse(6, test)
        assert paragraph_1.text == "a one liner of a paragraph"
        assert index1 == 3