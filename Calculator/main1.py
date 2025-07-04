class Calculator:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")
        self.operators = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        self.result = self.evaluate(self.expression)

    def evaluate(self, expr):
        while '(' in expr:
            start = expr.rfind('(')
            end = expr.find(')', start)
            if end == -1:
                raise ValueError("Mismatched parentheses")
            inner_result = self.evaluate(expr[start + 1:end])
            expr = expr[:start] + str(inner_result) + expr[end + 1:]
        return self.compute(expr)

    def compute(self, expr):
        import re
        tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/^]', expr)
        numbers = []
        ops = []

        def apply_op():
            b = numbers.pop()
            a = numbers.pop()
            op = ops.pop()
            result = {
                '+': a + b,
                '-': a - b,
                '*': a * b,
                '/': a / b,
                '^': a ** b
            }[op]
            numbers.append(result)

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.replace('.', '', 1).isdigit():
                numbers.append(float(token))
            else:
                while (ops and self.operators[token] <= self.operators[ops[-1]]):
                    apply_op()
                ops.append(token)
            i += 1

        while ops:
            apply_op()
        return numbers[0]

# --- Usage Example ---
if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter an equation: ")
            calc = Calculator(expression)
            print("Result:", calc.result)
        except Exception as e:
            print("Error:", e)
