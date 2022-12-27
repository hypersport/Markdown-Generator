import pytest
from mdmaker import Generator


def test_add_header(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

## Installing
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_header(2, 'Installing')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
