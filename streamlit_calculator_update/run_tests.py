import pytest
import io
import sys

def run_pytest_and_capture_output():
    buffer = io.StringIO()
    sys_stdout = sys.stdout
    sys.stderr = sys.stderr
    sys.stdout = buffer
    try:
        pytest.main(["-q", "test_calculator_engine.py"])
    finally:
        sys.stdout = sys_stdout
    return buffer.getvalue()
