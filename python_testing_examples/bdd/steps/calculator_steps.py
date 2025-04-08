from behave import given, when, then
from calculator import add

@given('the calculator is running')
def step_impl(context):
    pass  # No setup needed

@when('I add {a:d} and {b:d}')
def step_impl(context, a, b):
    context.result = add(a, b)

@then('the result should be {expected:d}')
def step_impl(context, expected):
    assert context.result == expected
