import pytest
from mdmaker import Generator

LINE1_CONTENT = 'This is a pure python library to generate Markdown.'
LINE2_CONTENT = 'It aims to generate Markdown files in a modular way with pure python.'


def test_add_line(generator: Generator) -> None:
    content = '''This is a pure python library to generate Markdown.  
It aims to generate Markdown files in a modular way with pure python.  
'''
    generator.add_line(LINE1_CONTENT)
    generator.add_line(LINE2_CONTENT)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_line_with_indents(generator: Generator) -> None:
    content = '''&nbsp;&nbsp;This is a pure python library to generate Markdown.  
&nbsp;&nbsp;It aims to generate Markdown files in a modular way with pure python.  
'''
    generator.add_line(LINE1_CONTENT, indents=2)
    generator.add_line(LINE2_CONTENT, indents=2)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_line(generator: Generator) -> None:
    content = '''**This is a pure python library to generate Markdown.**  
**It aims to generate Markdown files in a modular way with pure python.**  
'''
    generator.add_line(LINE1_CONTENT, is_bold=True)
    generator.add_line(LINE2_CONTENT, is_bold=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_italic_line(generator: Generator) -> None:
    content = '''*This is a pure python library to generate Markdown.*  
*It aims to generate Markdown files in a modular way with pure python.*  
'''
    generator.add_line(LINE1_CONTENT, is_italic=True)
    generator.add_line(LINE2_CONTENT, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_bold_italic_line(generator: Generator) -> None:
    content = '''***This is a pure python library to generate Markdown.***  
***It aims to generate Markdown files in a modular way with pure python.***  
'''
    generator.add_line(LINE1_CONTENT, is_bold=True, is_italic=True)
    generator.add_line(LINE2_CONTENT, is_bold=True, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
