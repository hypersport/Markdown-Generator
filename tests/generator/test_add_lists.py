import pytest
from mdmaker import Generator


def test_add_lists_ordered(generator: Generator) -> None:
    lists = {'is_ordered': True, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''1. First item
2. Second item
3. Third item
4. Fourth item
'''
    generator.add_lists(lists)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_lists_unordered(generator: Generator) -> None:
    lists = {'is_ordered': False, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''- First item
- Second item
- Third item
- Fourth item
'''
    generator.add_lists(lists)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_lists_nested(generator: Generator) -> None:
    lists = {'is_ordered': True, 'lists': ['First item', 'Second item', 'Third item', {
        'is_ordered': False, 'lists': ['Indented item', 'Indented item']}, 'Fourth item']}
    content = '''1. First item
2. Second item
3. Third item
    - Indented item
    - Indented item
4. Fourth item
'''
    generator.add_lists(lists)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_lists_in_blockquotes(generator: Generator) -> None:
    lists = {'is_ordered': True, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''> 1. First item
> 2. Second item
> 3. Third item
> 4. Fourth item
'''
    generator.add_lists_in_blockquotes(lists)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content


def test_add_lists_in_blockquotes_splitted(generator: Generator) -> None:
    lists = {'is_ordered': True, 'lists': [
        'First item', 'Second item', 'Third item', 'Fourth item']}
    content = '''> 1. First item
>
> 2. Second item
>
> 3. Third item
>
> 4. Fourth item
'''
    generator.add_lists_in_blockquotes(lists, True)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert content == file_content
