class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["+", "-", "*", "/"])
        stack = []

        for n in tokens:
            if n in operations:
                match n:
                    case "+":
                        res = stack[-2] + stack[-1]
                    case "-":
                        res = stack[-2] - stack[-1]
                    case "*":
                        res = stack[-2] * stack[-1]
                    case "/":
                        res = int(stack[-2] / stack[-1])
                del stack[-2:]
                stack.append(res)
            else:
                stack.append(int(n))
        return stack[0]