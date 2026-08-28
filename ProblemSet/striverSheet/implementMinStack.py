class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        if not self.stack:
            self.stack.append((value, value))
            return
        mini = min(self.getMin(), value)
        self.stack.append((value, mini))
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]
if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    print(f"Top element: {s.top()}")
    print(f"Minimum element: {s.getMin()}")
    s.pop()
    print(f"Top element after pop: {s.top()}")
    print(f"Minimum element after pop: {s.getMin()}")
    s.pop()
    print(f"Minimum element after pop: {s.getMin()}")