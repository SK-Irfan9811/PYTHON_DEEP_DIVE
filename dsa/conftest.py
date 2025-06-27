import pytest


@pytest.fixture
def fix_1():
    return True


@pytest.fixture
def fix_2(fix_1):
    return "I am fix_2"


def test_fixs(fix_2):
    print(fix_2)