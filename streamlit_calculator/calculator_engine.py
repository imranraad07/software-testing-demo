import ast
import operator

class StepExplainingCalculator:
    def __init__(self, precision=2):
        self.steps = []
        self.step_num = 1
        self.precision = precision

    def evaluate(self, expr):
        self.steps = []
        self.step_num = 1
        tree = ast.parse(expr, mode='eval')
        result = self._eval(tree.body)
        return round(result, self.precision), self.steps

    def _eval(self, node):
        ops = {
            ast.Add: ("+", operator.add),
            ast.Sub: ("-", operator.sub),
            ast.Mult: ("*", operator.mul),
            ast.Div: ("/", operator.truediv),
        }

        if isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)
            symbol, func = ops[type(node.op)]
            result = func(left, right)
            result = round(result, self.precision)
            self.steps.append(f"Step {self.step_num}: {left} {symbol} {right} = {result}")
            self.step_num += 1
            return result

        elif isinstance(node, ast.UnaryOp):
            return -self._eval(node.operand)

        elif isinstance(node, ast.Constant):
            return float(node.value)

        elif isinstance(node, ast.Num):
            return float(node.n)

        else:
            raise ValueError("Unsupported expression")
