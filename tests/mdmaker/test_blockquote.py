import pytest
from mdmaker import MdMaker


def test_blockquote(maker: MdMaker) -> None:
    content = '> This is not yet another library to generate HTML from Markdown.'
    blockquote = maker.blockquote(
        'This is not yet another library to generate HTML from Markdown.')
    assert content == blockquote


def test_multi_blockquotes(maker: MdMaker) -> None:
    content = '''> This is not yet another library to generate HTML from Markdown.
>
> This is a pure python library to generate Markdown.'''
    quotes = ['This is not yet another library to generate HTML from Markdown.',
              'This is a pure python library to generate Markdown.']
    blockquotes = maker.multi_blockquotes(quotes)
    assert content == blockquotes


def test_multi_blockquotes_splitted(maker: MdMaker) -> None:
    content = '''> This is not yet another library to generate HTML from Markdown.

> This is a pure python library to generate Markdown.'''
    quotes = ['This is not yet another library to generate HTML from Markdown.',
              'This is a pure python library to generate Markdown.']
    blockquotes = maker.multi_blockquotes(quotes, True)
    assert content == blockquotes
