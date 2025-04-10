import pytest
import sys 
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils import add, multiply, compute_total_with_fee

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 4) == 8

def test_compute_total_with_fee_calls_add(mocker):
    mock_add = mocker.patch("src.utils.add", return_value=10)
    result = compute_total_with_fee(2, 3, 10)  # Should be: 10 + 10% = 11
    assert result == 11
    mock_add.assert_called_once_with(2, 3)
