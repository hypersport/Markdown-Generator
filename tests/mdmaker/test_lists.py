import pytest
from mdmaker import MdMaker


def test_lists_ordered(maker: MdMaker) -> None:
    lists = {'is_ordered': True, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''1. First item
2. Second item
3. Third item
4. Fourth item'''
    assert content == maker.lists(lists)


def test_lists_unordered(maker: MdMaker) -> None:
    lists = {'is_ordered': False, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''- First item
- Second item
- Third item
- Fourth item'''
    assert content == maker.lists(lists)


def test_lists_nested(maker: MdMaker) -> None:
    lists = {'is_ordered': True, 'lists': ['First item', 'Second item', 'Third item', {
        'is_ordered': False, 'lists': ['Indented item', 'Indented item']}, 'Fourth item']}
    content = '''1. First item
2. Second item
3. Third item
    - Indented item
    - Indented item
4. Fourth item'''
    assert content == maker.lists(lists)


def test_lists_in_blockquotes(maker: MdMaker) -> None:
    lists = {'is_ordered': True, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''> 1. First item
> 2. Second item
> 3. Third item
> 4. Fourth item'''
    assert content == maker.lists_in_blockquotes(lists)


def test_lists_in_blockquotes_splitted(maker: MdMaker) -> None:
    lists = {'is_ordered': True, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''> 1. First item
>
> 2. Second item
>
> 3. Third item
>
> 4. Fourth item'''
    assert content == maker.lists_in_blockquotes(lists, True)
