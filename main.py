import pytest


def test_fail():
    assert False
def test_pass():
    assert 1 == 1
def double_integer(a: int) -> int:
    return a * 2



def add(a: float, b: float) -> float:
    return a + b




def test_double_integer():
    assert 4 == double_integer(2)

def test_add():
    assert 0.3 == add(0.1, 0.2)





def test_fail():
    assert False



