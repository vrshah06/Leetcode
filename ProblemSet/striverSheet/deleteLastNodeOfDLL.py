class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
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
def deleteLastNode(head):
    if head is None:
        return None
    if head.next is None:
        return None
    tail = head
    while tail.next:
        tail = tail.next
    tail.prev.next = None
    return head
def printList(head):
    while head:
        print(head.data, end="<->")
        head = head.next
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    print("Original List:")
    printList(head)
    head = deleteLastNode(head)
    print("\nList after deleting the last node:")
    printList(head)
        