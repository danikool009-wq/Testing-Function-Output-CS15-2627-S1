import pytest


def divide(a: float, b: float) -> float:
    """Divide a by b.

    :param a: The dividend.
    :param b: The divisor.
    :return: The quotient.
    """
    quotient = a / b
    return quotient


def test_divide():
    assert pytest.approx(3) == divide(0.3, 0.1)


def multiply(a: float, b: float) -> float:
    """Multiply a and b.

    :param a: The first factor.
    :param b: The second factor.
    :return: The product.
    """
    product = a * b
    return product


def test_multiply():
    assert multiply(2, 5) == 10



# Example 1
# The test is the problem.
# The function works correctly, but decimal values can cause precision issues.

# Example 2
# The function is the problem.
# It uses a a instead of a b.
# Change a a to a b.
