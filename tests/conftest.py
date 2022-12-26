import pytest
from mdmaker import MdMaker
from mdmaker import Generator


@pytest.fixture
def init_maker():
    return MdMaker()


@pytest.fixture
def init_generator(tmp_path):
    d = tmp_path/'sub'
    d.mkdir()
    p = d/'MdMaker.md'
    return Generator(p, 'w')
