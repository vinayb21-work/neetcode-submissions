class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                y, x = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                else:
                    if x > 0 and y > 0 or x < 0 and y < 0:
                        stack.append(int(x / y))
                    else:
                        stack.append(math.ceil(x / y))
                continue
            stack.append(int(token))
            # print(stack)
        return math.ceil(stack[0])

# 10, 6, -132
