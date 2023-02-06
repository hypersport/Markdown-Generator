import pytest
from mdmaker import Generator


def test_add_code_blocks_with_lang(generator: Generator) -> None:
    content = '''```python
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
```
'''
    codes = '''
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
'''
    generator.add_code_blocks(codes, 'python')
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert file_content == content


def test_add_code_blocks_without_lang(generator: Generator) -> None:
    content = '''```
sudo apt update
sudo apt upgrade -y
```
'''
    codes = '''
sudo apt update
sudo apt upgrade -y
'''
    generator.add_code_blocks(codes)
    generator.save_file()
    with open(generator.filename, 'r') as f:
        file_content = f.read()
    assert file_content == content
