class ArrayStack:
    def __init__(self,size=1000):
        self.stackArray = [0] * size
        self.top = -1
        self.size = size
    #Push operation
    def push(self, value):
        if self.top >= self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stackArray[self.top] = value
    #Pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return -1
        poppedValue = self.stackArray[self.top]
        self.top -= 1
        return poppedValue
    def isEmpty(self):
        return self.top == -1
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        return self.stackArray[self.top]
if __name__ == "__main__":
    stack = ArrayStack()
    commands = [ArrayStack,"push","push","top","pop","isEmpty"]
    inputs = [[],[5],[10],[],[],[]]
    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
        elif commands[i] == "pop":
            print(stack.pop())
        elif commands[i] == "top":
            print(stack.peek())
        elif commands[i] == "isEmpty":
            print(stack.isEmpty())
        elif commands[i] == ArrayStack:
            print("Stack created")