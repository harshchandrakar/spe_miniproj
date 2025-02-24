import pytest
import math
from scientific_calculator import ScientificCalculator

@pytest.fixture
def calculator():
    return ScientificCalculator()

def test_square_root(calculator):
    assert calculator.square_root(4) == 2
    assert calculator.square_root(9) == 3
    with pytest.raises(ValueError):
        calculator.square_root(-1)

def test_factorial(calculator):
    assert calculator.factorial(5) == 120
    assert calculator.factorial(0) == 1
    with pytest.raises(ValueError):
        calculator.factorial(-3)

def test_natural_log(calculator):
    assert calculator.natural_log(math.e) == pytest.approx(1)
    with pytest.raises(ValueError):
        calculator.natural_log(0)
    with pytest.raises(ValueError):
        calculator.natural_log(-10)

def test_power(calculator):
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(10, -1) == pytest.approx(0.1)
