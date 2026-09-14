class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def isPalindrome(head):
    stack = []
    current = head
    while current:
        stack.append(current.data)
        current = current.next
    current = head
    while current:
        if current.data != stack[-1]:
            return False
        stack.pop()
        current = current.next
    return True
def printList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    print("Linked List:")
    printList(head)

    if isPalindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")