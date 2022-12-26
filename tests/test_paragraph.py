import pytest
from mdmaker import MdMaker
from mdmaker import Generator


def test_paragraph(maker: MdMaker) -> None:
    content = 'This is not yet another library to generate HTML from Markdown.'
    paragraph = maker.paragraph(
        'This is not yet another library to generate HTML from Markdown.')
    assert content == paragraph


def test_paragraph_with_indents(maker: MdMaker) -> None:
    content = '&nbsp;&nbsp;This is not yet another library to generate HTML from Markdown.'
    paragraph = maker.paragraph(
        'This is not yet another library to generate HTML from Markdown.', indents=2)
    assert content == paragraph


def test_bold_paragraph(maker: MdMaker) -> None:
    content = '**This is not yet another library to generate HTML from Markdown.**'
    paragraph = maker.paragraph(
        'This is not yet another library to generate HTML from Markdown.', is_bold=True)
    assert content == paragraph


def test_italic_paragraph(maker: MdMaker) -> None:
    content = '*This is not yet another library to generate HTML from Markdown.*'
    paragraph = maker.paragraph(
        'This is not yet another library to generate HTML from Markdown.', is_italic=True)
    assert content == paragraph


def test_bold_italic_paragraph(maker: MdMaker) -> None:
    content = '***This is not yet another library to generate HTML from Markdown.***'
    paragraph = maker.paragraph(
        'This is not yet another library to generate HTML from Markdown.', is_bold=True, is_italic=True)
    assert content == paragraph


def test_add_paragraph_begin(generator: Generator) -> None:
    content = '''This is not yet another library to generate HTML from Markdown.
'''
    generator.add_paragraph(
        'This is not yet another library to generate HTML from Markdown.')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_paragraph_middle(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

This is not yet another library to generate HTML from Markdown.
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_paragraph(
        'This is not yet another library to generate HTML from Markdown.')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_paragraph_with_indents(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

&nbsp;&nbsp;This is not yet another library to generate HTML from Markdown.
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_paragraph(
        'This is not yet another library to generate HTML from Markdown.', indents=2)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_paragraph(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

**This is not yet another library to generate HTML from Markdown.**
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_paragraph(
        'This is not yet another library to generate HTML from Markdown.', is_bold=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_italic_paragraph(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

*This is not yet another library to generate HTML from Markdown.*
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_paragraph(
        'This is not yet another library to generate HTML from Markdown.', is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_italic_paragraph(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

***This is not yet another library to generate HTML from Markdown.***
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_paragraph(
        'This is not yet another library to generate HTML from Markdown.', is_bold=True, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content