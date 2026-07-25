class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for x in tokens:
            if x == "+":
                stack.append(stack.pop() + stack.pop())
                print("add")
                print(stack)
            elif x == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                print("sub")
                print(stack)
            elif x == "*":
                stack.append(stack.pop() * stack.pop())
                print("mul")
                print(stack)
            elif x == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
                print("div")
                print(stack)
            else:
                stack.append(int(x))
                print(stack)
        return stack[0]