import pytest


def test_header(init_maker):
    header = '# Markdown Maker and Generator'
    assert header == init_maker.header(1, 'Markdown Maker and Generator')

    header = '## Installing'
    assert header == init_maker.header(2, 'Installing')


def test_add_header(init_generator):
    init_generator.add_header(1, 'Markdown Maker and Generator')
    init_generator.add_header(2, 'Installing')
    init_generator.save_file()
    content = '''# Markdown Maker and Generator

## Installing
'''
    with open(init_generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
