class ArrayQueue:
    def __init__(self):
        self.queueArray = [0] * 1000
        self.front = -1
        self.rear = -1
        self.currentSize = 0
        self.maxSize = 10
    #Enqueue operation
    def enqueue(self, value):
        if self.currentSize >= self.maxSize:
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.maxSize
        self.queueArray[self.rear] = value
        self.currentSize += 1
    #Dequeue operation
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return -1
        dequeuedValue = self.queueArray[self.front]
        self.front = (self.front + 1) % self.maxSize
        self.currentSize -= 1
        if self.currentSize == 0:
            self.front = -1
            self.rear = -1
        return dequeuedValue
    def isEmpty(self):
        return self.currentSize == 0

if __name__ == "__main__":
    queue = ArrayQueue()
    commands = [ArrayQueue,"enqueue","enqueue","dequeue","isEmpty"]
    inputs = [[],[5],[10],[],[]]
    for i in range(len(commands)):
        if commands[i] == "enqueue":
            queue.enqueue(inputs[i][0])
        elif commands[i] == "dequeue":
            print(queue.dequeue())
        elif commands[i] == "isEmpty":
            print(queue.isEmpty())
        elif commands[i] == ArrayQueue:
            print("Queue created")