import pytest
from calculator.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_mixed(self):
        assert add(-1, 5) == 4

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_positive_result(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(2, 5) == -3

    def test_zero(self):
        assert subtract(5, 5) == 0


class TestMultiply:
    def test_positive(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative(self):
        assert multiply(-2, 3) == -6

    def test_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_negative(self):
        assert divide(-9, 3) == -3.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
