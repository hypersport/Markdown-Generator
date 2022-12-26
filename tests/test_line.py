import pytest
from mdmaker import MdMaker
from mdmaker import Generator


def test_line(maker: MdMaker) -> None:
    content = 'This is a pure python library to generate Markdown.  '
    line = maker.line('This is a pure python library to generate Markdown.')
    assert content == line


def test_line_with_indents(maker: MdMaker) -> None:
    content = '&nbsp;&nbsp;This is a pure python library to generate Markdown.  '
    line = maker.line(
        'This is a pure python library to generate Markdown.', indents=2)
    assert content == line


def test_bold_line(maker: MdMaker) -> None:
    content = '**This is a pure python library to generate Markdown.**  '
    line = maker.line(
        'This is a pure python library to generate Markdown.', is_bold=True)
    assert content == line


def test_italic_line(maker: MdMaker) -> None:
    content = '*This is a pure python library to generate Markdown.*  '
    line = maker.line(
        'This is a pure python library to generate Markdown.', is_italic=True)
    assert content == line


def test_bold_italic_line(maker: MdMaker) -> None:
    content = '***This is a pure python library to generate Markdown.***'
    line = maker.line(
        'This is a pure python library to generate Markdown.', is_bold=True, is_italic=True)
    assert content == line


def test_add_line_begin(generator: Generator) -> None:
    content = '''This is a pure python library to generate Markdown.
'''
    generator.add_line(
        'This is a pure python library to generate Markdown.')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_line_middle(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

This is a pure python library to generate Markdown.
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_line(
        'This is a pure python library to generate Markdown.')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_line_with_indents(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

&nbsp;&nbsp;This is a pure python library to generate Markdown.
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_line(
        'This is a pure python library to generate Markdown.', indents=2)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_line(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

**This is a pure python library to generate Markdown.**
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_line(
        'This is a pure python library to generate Markdown.', is_bold=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_italic_line(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

*This is a pure python library to generate Markdown.*
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_line(
        'This is a pure python library to generate Markdown.', is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_italic_line(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

***This is a pure python library to generate Markdown.***
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_line(
        'This is a pure python library to generate Markdown.', is_bold=True, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
