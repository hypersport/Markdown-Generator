import pytest
from mdmaker import MdMaker

LINE_CONTENT = 'This is a pure python library to generate Markdown.'


def test_line(maker: MdMaker) -> None:
    content = 'This is a pure python library to generate Markdown.  '
    line = maker.line(LINE_CONTENT)
    assert content == line


def test_line_with_indents(maker: MdMaker) -> None:
    content = '&nbsp;&nbsp;This is a pure python library to generate Markdown.  '
    line = maker.line(LINE_CONTENT, indents=2)
    assert content == line


def test_bold_line(maker: MdMaker) -> None:
    content = '**This is a pure python library to generate Markdown.**  '
    line = maker.line(LINE_CONTENT, is_bold=True)
    assert content == line


def test_italic_line(maker: MdMaker) -> None:
    content = '*This is a pure python library to generate Markdown.*  '
    line = maker.line(LINE_CONTENT, is_italic=True)
    assert content == line


def test_bold_italic_line(maker: MdMaker) -> None:
    content = '***This is a pure python library to generate Markdown.***  '
    line = maker.line(LINE_CONTENT, is_bold=True, is_italic=True)
    assert content == line


def test_multi_lines(maker: MdMaker) -> None:
    content = '''This is a pure python library to generate Markdown.  
It aims to generate Markdown files in a modular way with pure python.  '''
    lines = ['This is a pure python library to generate Markdown.',
             'It aims to generate Markdown files in a modular way with pure python.']
    line = maker.multi_lines(lines)
    assert content == line
