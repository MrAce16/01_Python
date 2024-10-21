# import pytest


# def test_para(a, b, results
#               [
#                   (1, 2, 3),
#                   (10, 20, 30)
#               ]

#               ):
#     assert a+b == results


import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 20, 30)
])
def test_add(a, b, expected):
    assert a + b == expected
