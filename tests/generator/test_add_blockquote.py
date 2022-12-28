import pytest
from mdmaker import Generator


def test_add_blockquote_begin(generator: Generator) -> None:
    content = '''> This is not yet another library to generate HTML from Markdown.
'''
    generator.add_blockquote(
        'This is not yet another library to generate HTML from Markdown.')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_blockquote(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

> This is not yet another library to generate HTML from Markdown.
'''
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_blockquote(
        'This is not yet another library to generate HTML from Markdown.')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_multi_blockquotes_begin(generator: Generator) -> None:
    content = '''> This is not yet another library to generate HTML from Markdown.
>
> This is a pure python library to generate Markdown.
'''
    quotes = ['This is not yet another library to generate HTML from Markdown.',
              'This is a pure python library to generate Markdown.']
    generator.add_multi_blockquotes(quotes)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_multi_blockquotes(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

> This is not yet another library to generate HTML from Markdown.
>
> This is a pure python library to generate Markdown.
'''
    quotes = ['This is not yet another library to generate HTML from Markdown.',
              'This is a pure python library to generate Markdown.']
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_multi_blockquotes(quotes)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_multi_blockquotes_splitted_begin(generator: Generator) -> None:
    content = '''> This is not yet another library to generate HTML from Markdown.

> This is a pure python library to generate Markdown.
'''
    quotes = ['This is not yet another library to generate HTML from Markdown.',
              'This is a pure python library to generate Markdown.']
    generator.add_multi_blockquotes(quotes, True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_multi_splitted_blockquotes(generator: Generator) -> None:
    content = '''# Markdown Maker and Generator

> This is not yet another library to generate HTML from Markdown.

> This is a pure python library to generate Markdown.
'''
    quotes = ['This is not yet another library to generate HTML from Markdown.',
              'This is a pure python library to generate Markdown.']
    generator.add_header(1, 'Markdown Maker and Generator')
    generator.add_multi_blockquotes(quotes, True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
