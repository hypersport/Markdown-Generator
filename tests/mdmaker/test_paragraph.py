import pytest
from mdmaker import MdMaker

CONTENT = 'This is not yet another library to generate HTML from Markdown.'
HEADER = 'Markdown Maker and Generator'


def test_paragraph(maker: MdMaker) -> None:
    content = CONTENT
    paragraph = maker.paragraph(CONTENT)
    assert content == paragraph


def test_paragraph_with_indents(maker: MdMaker) -> None:
    content = '&nbsp;&nbsp;This is not yet another library to generate HTML from Markdown.'
    paragraph = maker.paragraph(CONTENT, indents=2)
    assert content == paragraph


def test_bold_paragraph(maker: MdMaker) -> None:
    content = '**This is not yet another library to generate HTML from Markdown.**'
    paragraph = maker.paragraph(CONTENT, is_bold=True)
    assert content == paragraph


def test_italic_paragraph(maker: MdMaker) -> None:
    content = '*This is not yet another library to generate HTML from Markdown.*'
    paragraph = maker.paragraph(CONTENT, is_italic=True)
    assert content == paragraph


def test_bold_italic_paragraph(maker: MdMaker) -> None:
    content = '***This is not yet another library to generate HTML from Markdown.***'
    paragraph = maker.paragraph(CONTENT, is_bold=True, is_italic=True)
    assert content == paragraph


def test_multi_paragraphs(maker: MdMaker) -> None:
    content = '''This is not yet another library to generate HTML from Markdown.

This is a pure python library to generate Markdown.'''
    paragraphs = ['This is not yet another library to generate HTML from Markdown.',
                  'This is a pure python library to generate Markdown.']
    paragraph = maker.multi_paragraphs(paragraphs)
    assert content == paragraph
