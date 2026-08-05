from text import Text
from elements.inline.plain_text import PlainText
from elements.inline.italic import Italic
from elements.inline.bold import Bold
from elements.inline.strikethrough import Strikethrough
from elements.inline.link import Link


def test_render_inline_html():
    test_text = Text([Bold("This"), PlainText(" is sooo "), Italic("pretty"), PlainText("!")])
    assert test_text.render_html() == "<strong>This</strong> is sooo <em>pretty</em>!"


def test_render_italic():
    assert Italic("test").render_html() == "<em>test</em>"


def test_render_bold():
    assert Bold("test").render_html() == "<strong>test</strong>"


def test_render_strikethrough():
    assert Strikethrough("test").render_html() == "<del>test</del>"


def test_render_link():
    assert Link("test", "test.com").render_html() == "<a href='test.com'>test</a>"
