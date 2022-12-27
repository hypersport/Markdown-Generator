import pytest
from mdmaker import Generator


def test_add_text(generator: Generator):
    content = ' Markdown'
    generator.add_text('Markdown')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_bold_text(generator: Generator):
    content = ' **Markdown**'
    generator.add_text('Markdown', is_bold=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_italic_text(generator: Generator):
    content = ' *Markdown*'
    generator.add_text('Markdown', is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_bold_italic_text(generator: Generator):
    content = ' ***Markdown***'
    generator.add_text('Markdown', is_bold=True, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_mix_text(generator: Generator):
    content = ' Normal **Bold** *Italic* ***Bold and Italic***'
    generator.add_text('Normal')
    generator.add_text('Bold', is_bold=True)
    generator.add_text('Italic', is_italic=True)
    generator.add_text('Bold and Italic', is_bold=True, is_italic=True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
