import pytest
from mdmaker import MdMaker
from mdmaker import Generator


def test_header(maker: MdMaker) -> None:
    header = '# Markdown Maker and Generator'
    assert header == maker.header(1, 'Markdown Maker and Generator')

    header = '## Installing'
    assert header == maker.header(2, 'Installing')


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
