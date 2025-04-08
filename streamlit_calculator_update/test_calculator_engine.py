import pytest
from calculator_engine import StepExplainingCalculator

@pytest.fixture
def calc():
    return StepExplainingCalculator(precision=2)

def test_addition(calc):
    result, steps = calc.evaluate("2 + 3")
    assert result == 5
    assert steps == ["Step 1: 2.0 + 3.0 = 5.0"]

def test_operator_precedence(calc):
    result, steps = calc.evaluate("2 + 3 * 4")
    assert result == 14
    assert steps == [
        "Step 1: 3 * 4 = 12",
        "Step 2: 2 + 12 = 14"
    ]

def test_parentheses(calc):
    result, steps = calc.evaluate("(2 + 3) * 4")
    assert result == 20
    assert steps == [
        "Step 1: 2 + 3 = 5",
        "Step 2: 5 * 4 = 20"
    ]

def test_scientific_notation(calc):
    result, steps = calc.evaluate("1e2 + 2e1")
    assert result == 120.0
    assert "Step 1: 100.0 + 20.0 = 120.0" in steps[0]

def test_division_and_precision():
    calc = StepExplainingCalculator(precision=3)
    result, steps = calc.evaluate("10 / 3")
    assert result == 3.333
    assert steps == ["Step 1: 10.0 / 3.0 = 3.333"]

def test_invalid_expression():
    calc = StepExplainingCalculator()
    with pytest.raises(ValueError):
        calc.evaluate("2 ++ 2")

def test_unary_negative(calc):
    result, steps = calc.evaluate("-5 + 8")
    assert result == 3
