import pytest
from text import Text
from elements.inline.plain_text import PlainText
from elements.inline.italic import Italic

def test_render_inline_html():
    assert Text([PlainText("This is sooo "), Italic("pretty"), PlainText("!")]).render_html() == "This is sooo <em>pretty</em>!"
