# calculator.py
import math
import re

class Calculator:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")
        self.constants = {'pi': math.pi, 'e': math.e}
        self.operators = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
        self.functions = {
            'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos,
            'tan': math.tan, 'log': math.log, 'exp': math.exp,
            'abs': abs, 'round': round, 'floor': math.floor,
            'ceil': math.ceil, 'max': max, 'min': min
        }
        self.result = self.evaluate(self.expression)

    def evaluate(self, expr):
        for const, val in self.constants.items():
            expr = re.sub(rf'\b{const}\b', str(val), expr)

        while '(' in expr:
            start = expr.rfind('(')
            end = expr.find(')', start)
            if end == -1:
                raise ValueError("Mismatched parentheses")
            inner = expr[start + 1:end]
            args = [self.evaluate(arg) for arg in self.split_args(inner)]
            func_match = re.match(r'[a-zA-Z_]+$', expr[:start])
            if func_match:
                func_name = func_match.group()
                if func_name not in self.functions:
                    raise ValueError(f"Unsupported function: {func_name}")
                result = self.functions[func_name](*map(float, args))
                expr = expr[:start - len(func_name)] + str(result) + expr[end + 1:]
            else:
                expr = expr[:start] + str(args[0]) + expr[end + 1:]
        return self.compute(expr)

    def split_args(self, arg_str):
        args, current, depth = [], '', 0
        for char in arg_str:
            if char == ',' and depth == 0:
                args.append(current)
                current = ''
            else:
                if char == '(': depth += 1
                if char == ')': depth -= 1
                current += char
        if current: args.append(current)
        return args

    def compute(self, expr):
        tokens = re.findall(r'-?\d+\.\d+|-?\d+|[+\-*/^]', expr)
        numbers, ops = [], []

        def apply_op():
            b = numbers.pop()
            a = numbers.pop()
            op = ops.pop()
            operations = {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b}
            numbers.append(operations[op])

        for token in tokens:
            if re.fullmatch(r'-?\d+(\.\d+)?', token):
                numbers.append(float(token))
            else:
                while ops and self.operators[token] <= self.operators[ops[-1]]:
                    apply_op()
                ops.append(token)
        while ops:
            apply_op()
        return numbers[0]
