# Function 1
import pytest


def double_number(a):
    return a * 2


# Tests for Function 1
def test_double_number_1():
    assert double_number(5) == 10


def test_double_number_2():
    assert double_number(8) == 16


# Function 2
def add_ten(a):
    return a + 10


# Tests for Function 2
def test_add_ten_1():
    assert add_ten(5) == 15


def test_add_ten_2():
    assert add_ten(20) == 30


# Function 3
def rectangle_area(length, width):
    return length * width


# Tests for Function 3
def test_rectangle_area_1():
    assert rectangle_area(5, 4) == 20


def test_rectangle_area_2():
    assert pytest.approx(10.5) == rectangle_area(3.5, 3)