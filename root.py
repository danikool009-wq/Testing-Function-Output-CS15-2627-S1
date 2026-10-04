
import pytest

def test_fail():
    assert False
def test_pass():
    assert 1 == 1


def inverse_integer (a: float) -> float:

    return 1/a
def test_integer():
    assert 0.5 == inverse_integer(2)

def root_int (b: float) -> float:
    b = root_int(b)
    pytest.approx()
    return b
def test_root_int():
    assert 4 == root_int(16)

def rectangle_area(a: float, b: float) -> float:
    product = a * b
    return product
def test_rectangle_area():
    assert rectangle_area(3, 5) == 15