import pytest
from text import Text
from elements.inline.plain_text import PlainText
from elements.inline.italic import Italic
from elements.inline.bold import Bold

def test_render_inline_html():
    assert Text([Bold("This"),PlainText(" is sooo "), Italic("pretty"), PlainText("!")]).render_html() == "<strong>This</strong> is sooo <em>pretty</em>!"


def test_render_italic():
    assert Italic("test").render_html() == "<em>test</em>"

def test_render_bold():
    assert Bold("test").render_html() == "<strong>test</strong>"