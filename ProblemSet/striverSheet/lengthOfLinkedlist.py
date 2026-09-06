class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def insertAtHead(self, head, data):
        #create a new node with the given data
        newNode = Node(data)
        #link the new node to the current head of the linked list
        newNode.next = head
        return newNode
    def lengthOfLinkedList(self, head):
        #initialize a counter to keep track of the length
        count = 0
        #traverse the linked list and increment the counter for each node
        current = head
        while current:
            count += 1
            current = current.next
        return count
if __name__ == "__main__":
    linkedList = LinkedList()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head= linkedList.insertAtHead(head, 10)
    #calculate the length of the linked list
    length = linkedList.lengthOfLinkedList(head)
    print("Length of the linked list:", length)
