class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insertAtEnd(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = newNode
    return head
def reverseLL(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head
def printList(head):
    while head:
        print(head.data, end="->")
        head = head.next
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    print("Original List:")
    printList(head)
    head = reverseLL(head)
    print("\nList after reversing:")
    printList(head)
