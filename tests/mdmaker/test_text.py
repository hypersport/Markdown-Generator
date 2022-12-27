import pytest
from mdmaker import MdMaker


def test_text(maker: MdMaker):
    content = ' Markdown'
    assert content == maker.text('Markdown')


def test_bold_text(maker: MdMaker):
    content = ' **Markdown**'
    assert content == maker.text('Markdown', is_bold=True)


def test_italic_text(maker: MdMaker):
    content = ' *Markdown*'
    assert content == maker.text('Markdown', is_italic=True)


def test_bold_italic_text(maker: MdMaker):
    content = ' ***Markdown***'
    assert content == maker.text('Markdown', is_bold=True, is_italic=True)


def test_mix_text(maker: MdMaker):
    content = ' Normal **Bold** *Italic* ***Bold and Italic***'
    normal = maker.text('Normal')
    bold = maker.text('Bold', is_bold=True)
    italic = maker.text('Italic', is_italic=True)
    bold_and_italic = maker.text(
        'Bold and Italic', is_bold=True, is_italic=True)
    assert content == normal+bold+italic+bold_and_italic
