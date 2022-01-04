class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.length = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1
        if self.min_stack and val <= self.min_stack[-1]:
            self.min_stack.append(val)
        elif len(self.min_stack) == 0:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.length > 0:
            val = self.stack.pop()
            self.length -= 1
            if self.min_stack and self.min_stack[-1] == val:
                self.min_stack.pop()
    def top(self) -> int:
        if self.length > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()