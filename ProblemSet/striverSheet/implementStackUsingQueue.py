from queue import Queue
class QueueStack:
    def __init__(self):
        self.q = Queue()
    def push(self, value):
        s = self.q.qsize()
        self.q.put(value)
        for _ in range(s):
            self.q.put(self.q.get())
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return -1
        n = self.q.queue[0]
        self.q.get()
        return n
    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        return self.q.queue[0]
    def isEmpty(self):
        return self.q.empty()
if __name__ == "__main__":
    stack = QueueStack()
    commands = [QueueStack,"push","push","top","pop","isEmpty"]
    inputs = [[],[5],[10],[],[],[]]
    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
        elif commands[i] == "pop":
            print(stack.pop())
        elif commands[i] == "top":
            print(stack.top())
        elif commands[i] == "isEmpty":
            print(stack.isEmpty())
        elif commands[i] == QueueStack:
            print("Stack created")