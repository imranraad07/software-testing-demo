import pytest
import sys 
import os 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pytest_bdd import scenario, given, when, then, scenarios, parsers
import src.utils as utils

# Link the feature file
scenarios("../features/addition.feature")


@pytest.fixture
def context():
    return {}

@given(parsers.parse("I have numbers {x:d} and {y:d}"))
def step_given_numbers(x, y, context):
    context["x"] = x
    context["y"] = y

@when("I add them")
def step_when_add(context):
    context["result"] = utils.add(context["x"], context["y"])

@then("the result should be 5")
def step_then_result(context):
    assert context["result"] == 5




# @pytest.fixture
# def number_list():
#     return []

# @given("I have number 3")
# def step_given_num1(number_list):
#     number_list.append(3)

# @given("I have number 4")
# def step_given_num2(number_list):
#     number_list.append(4)

# @given("I have number 5")
# def step_given_num3(number_list):
#     number_list.append(5)

# @when("I add all the numbers")
# def step_when_add_all(number_list):
#     number_list.append(sum(number_list))  # Store result at the end

# @then("the result should be 12")
# def step_then_check(number_list):
#     assert number_list[-1] == 12
