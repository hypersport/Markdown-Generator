import pytest
from pathlib import PosixPath
from mdmaker import MdMaker
from mdmaker import Generator


@pytest.fixture
def maker() -> MdMaker:
    return MdMaker()


@pytest.fixture
def generator(tmp_path: PosixPath) -> Generator:
    d = tmp_path/'sub'
    d.mkdir()
    p = d/'MdMaker.md'
    return Generator(p, 'w')
