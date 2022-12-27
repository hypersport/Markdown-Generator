import pytest
from mdmaker import MdMaker


def test_header(maker: MdMaker) -> None:
    header = '# Markdown Maker and Generator'
    assert header == maker.header(1, 'Markdown Maker and Generator')

    header = '## Installing'
    assert header == maker.header(2, 'Installing')
