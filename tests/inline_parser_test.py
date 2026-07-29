import pytest
from elements.inline.italic import Italic
from elements.inline.bold import Bold
from elements.inline.plain_text import PlainText
from inline_context import InlineContext
from text import Text

ELEMENT_LIST = [Bold, Italic]
def test_plain_text():
    inline_context = InlineContext("boring text", ELEMENT_LIST, 0)

    assert inline_context.identify_current_inline_element() == PlainText


def test_italic():
    inline_context = InlineContext("*test*", ELEMENT_LIST, 0)

    assert inline_context.identify_current_inline_element() == Italic
    italic_test = Italic.parse(inline_context)

    assert italic_test.content == "test"

def test_bold():
    inline_context = InlineContext("**test**", ELEMENT_LIST, 0)
    assert inline_context.identify_current_inline_element() == Bold

    bold_test = Bold.parse(inline_context)
    assert bold_test.content == "test"


def test_text():
    text = Text.parse("Now we have a *pretty* test don't **we**?")
    assert type(text.text_items[0]) == PlainText
    assert len(text.text_items) == 5
