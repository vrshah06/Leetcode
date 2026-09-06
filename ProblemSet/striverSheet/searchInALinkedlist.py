class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def insertAtHead(self, head, data):
        newNode = Node(data)
        newNode.next = head
        return newNode
    #to delete the last node of the linked list
    def deleteAtLast(self, head):
        #if the linked list is empty, return None
        if head is None:
            return None
        #if the linked list has only one node, delete it and return None
        if head.next is None:
            return None
        #traverse the linked list to find the second last node
        current = head
        while current.next.next:
            current = current.next
        #delete the last node
        current.next = None
        return head
    def printList(self, head):
        current = head
        while current:
            print(current.data, end="->")
            current = current.next
        print()
    def searchInLinkedList(self, head, target):
        #traverse the linked list to find the target value
        current = head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
if __name__ == "__main__":
    linkedList = LinkedList()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    #print the linked list
    print("Linked List:")
    linkedList.printList(head)
    #search for a target value in the linked list
    target = 3
    found = linkedList.searchInLinkedList(head, target)
    if found:
        print(f"Value {target} found in the linked list.")
    else:
        print(f"Value {target} not found in the linked list.")