from behave import given, when, then
from calculator_engine import StepExplainingCalculator

@given('the calculator is running')
def step_given_calculator(context):
    context.calc = StepExplainingCalculator()

@given('the calculator is running with precision {precision:d}')
def step_given_calc_precision(context, precision):
    context.calc = StepExplainingCalculator(precision=precision)

@when('I add {a:d} and {b:d}')
def step_when_add(context, a, b):
    context.result, context.steps = context.calc.evaluate(f"{a} + {b}")

@when('I evaluate "{expression}"')
def step_when_eval_expression(context, expression):
    context.result, context.steps = context.calc.evaluate(expression)

@then('the result should be {expected:g}')
def step_then_result(context, expected):
    assert round(context.result, 5) == round(expected, 5)
