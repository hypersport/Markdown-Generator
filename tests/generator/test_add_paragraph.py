import pytest
from mdmaker import Generator

CONTENT = 'This is not yet another library to generate HTML from Markdown.'
HEADER = 'Markdown Maker and Generator'


def test_add_paragraph_begin(generator: Generator) -> None:
    content = '''This is not yet another library to generate HTML from Markdown.
'''
    generator.add_paragraph(CONTENT)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_paragraph(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

This is not yet another library to generate HTML from Markdown.
'''
    generator.add_header(1, HEADER)
    generator.add_paragraph(CONTENT)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_paragraph_with_indents(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

&nbsp;&nbsp;This is not yet another library to generate HTML from Markdown.
'''
    generator.add_header(1, HEADER)
    generator.add_paragraph(CONTENT, indents=2)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_paragraph(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

**This is not yet another library to generate HTML from Markdown.**
'''
    generator.add_header(1, HEADER)
    generator.add_paragraph(CONTENT, is_bold=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_italic_paragraph(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

*This is not yet another library to generate HTML from Markdown.*
'''
    generator.add_header(1, HEADER)
    generator.add_paragraph(CONTENT, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_italic_paragraph(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

***This is not yet another library to generate HTML from Markdown.***
'''
    generator.add_header(1, HEADER)
    generator.add_paragraph(CONTENT, is_bold=True, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_multi_paragraphs(generator: Generator) -> None:
    content = '''This is not yet another library to generate HTML from Markdown.

This is a pure python library to generate Markdown.
'''
    paragraphs = ['This is not yet another library to generate HTML from Markdown.',
                  'This is a pure python library to generate Markdown.']
    generator.add_multi_paragraphs(paragraphs)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
