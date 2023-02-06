import pytest
from mdmaker import MdMaker


def test_code(maker: MdMaker) -> None:
    content = '`python -m pip install -U mdmaker`'
    assert content == maker.code('python -m pip install -U mdmaker')


def test_inline_code(maker: MdMaker) -> None:
    content = 'At the command prompt, type `nano`'
    text = maker.paragraph('At the command prompt, type')
    text += maker.code('nano', 1)
    assert content == text


def test_code_blocks_with_lang(maker: MdMaker) -> None:
    content = '''```python
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
```'''
    codes = '''
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
'''
    assert content == maker.code_blocks(codes, 'python')


def test_code_blocks_without_lang(maker: MdMaker) -> None:
    content = '''```
sudo apt update
sudo apt upgrade -y
```'''
    codes = '''
sudo apt update
sudo apt upgrade -y
'''
    assert content == maker.code_blocks(codes)
