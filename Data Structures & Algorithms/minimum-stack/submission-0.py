class MinStack:

    def __init__(self):
        self.minList = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minList:
            self.minList.append(val)
        elif val <= self.minList[-1]:
            self.minList.append(val)

    def pop(self) -> None:
        final = self.stack.pop()
        if final == self.minList[-1]:
            self.minList.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minList[-1]
