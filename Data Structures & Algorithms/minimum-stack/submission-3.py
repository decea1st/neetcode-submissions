class MinStack:

    def __init__(self):
        self.stack = [] # -2, 0
        self.currMin = float('inf')
        self.minOrder = [self.currMin]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.currMin = min(val, self.currMin)
        self.minOrder.append(self.currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minOrder.pop()
        self.currMin = self.minOrder[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minOrder[-1]
