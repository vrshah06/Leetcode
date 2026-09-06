class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def insertAtHead(self, head, data):
        newNode = Node(data)
        newNode.next = head
        return newNode
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
if __name__ == "__main__":
    linkedList = LinkedList()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    #print the linked list before deletion
    print("Linked List before deletion:")
    linkedList.printList(head)
    #delete the last node of the linked list
    head = linkedList.deleteAtLast(head)
    #print the linked list after deletion
    print("Linked List after deletion:")
    linkedList.printList(head)
    