import pytest
from mdmaker import MdMaker


def test_text(maker: MdMaker) -> None:
    content = ' Markdown'
    text = maker.text('Markdown')
    assert content == text


def test_bold_text(maker: MdMaker) -> None:
    content = ' **Markdown**'
    text = maker.text('Markdown', is_bold=True)
    assert content == text


def test_italic_text(maker: MdMaker) -> None:
    content = ' *Markdown*'
    text = maker.text('Markdown', is_italic=True)
    assert content == text


def test_bold_italic_text(maker: MdMaker) -> None:
    content = ' ***Markdown***'
    text = maker.text('Markdown', is_bold=True, is_italic=True)
    assert content == text


def test_mix_text(maker: MdMaker) -> None:
    content = ' Normal **Bold** *Italic* ***Bold and Italic***'
    normal = maker.text('Normal')
    bold = maker.text('Bold', is_bold=True)
    italic = maker.text('Italic', is_italic=True)
    bold_and_italic = maker.text(
        'Bold and Italic', is_bold=True, is_italic=True)
    text = normal+bold+italic+bold_and_italic
    assert content == text
