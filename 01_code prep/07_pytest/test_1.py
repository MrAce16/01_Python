import math
import pytest


def test_root():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.skip
def test_sqaure():
    num = 7
    assert 7*7 == 49


def test_equality():
    assert 11 == 11