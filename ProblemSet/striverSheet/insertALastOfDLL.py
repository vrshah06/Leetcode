class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def printList(head):
    while head:
        print(head.data, end="<->")
        head = head.next
def insertAtEnd(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = newNode
    newNode.prev = tail
    return head
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    print("Original List:")
    printList(head)
    data = 4
    head = insertAtEnd(head, data)
    print("\nList after inserting", data, "at the end:")
    printList(head)
