class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def segregateEvenOdd(head):
    if head is None or head.next is None:
        return head
    even_head = even_tail = None
    odd_head = odd_tail = None
    current = head
    while current:
        if current.data % 2 == 0:
            if even_head is None:
                even_head = even_tail = current
            else:
                even_tail.next = current
                even_tail = current
        else:
            if odd_head is None:
                odd_head = odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
        current = current.next
    if even_head is None:
        return odd_head
    if odd_head is None:
        return even_head
    # Connect even and odd lists 
    even_tail.next = odd_head
    odd_tail.next = None
    return even_head
def printList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original Linked List:")
    printList(head)

    segregated_head = segregateEvenOdd(head)

    print("Linked List after segregating even and odd nodes:")
    printList(segregated_head)