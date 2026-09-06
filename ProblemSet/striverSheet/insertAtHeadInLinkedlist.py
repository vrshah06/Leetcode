class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    #to insert a new node at the head of the linked list
    def insertAtHead(self, head, data):
        #create a new node with the given data
        newNode = Node(data)
        #link the new node to the current head of the linked list
        newNode.next = head
        return newNode
    def printList(self, head):
        #traverse the linked list and print the data of each node
        current = head
        while current:
            print(current.data, end="->")
            current = current.next
          # for a new line after printing the list
        print()
if __name__ == "__main__":
    linkedList = LinkedList()
    head = Node(1)
    head.next = Node(2)
    #insert nodes at the head of the linked list
    head = linkedList.insertAtHead(head, 10)
    head = linkedList.insertAtHead(head, 20)
    head = linkedList.insertAtHead(head, 30)
    #print the linked list
    linkedList.printList(head)