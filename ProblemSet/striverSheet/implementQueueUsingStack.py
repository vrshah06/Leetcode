class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, item):
        self.stack1.append(item)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]       
    def is_empty(self):
        print(f"Is queue empty: {len(self.stack1) == 0}")
if __name__ == "__main__":
    queue = StackQueue()
    commands = ["StackQueue", "push", "push", "pop", "peek", "isEmpty"]
    inputs = [[], [4], [8], [], [], []]
    for command, input in zip(commands, inputs):
        if command == "StackQueue":
            queue = StackQueue()
            print("Queue created")
        elif command == "push":
            queue.enqueue(input[0])
            print(f"Enqueued element: {input[0]}")
        elif command == "pop":
            queue.dequeue()
        elif command == "peek":
            queue.peek()
        elif command == "isEmpty":
            queue.is_empty()