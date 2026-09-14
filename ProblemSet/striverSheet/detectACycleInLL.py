class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def detectCycle(head):
        temp = head
        nodemap = {}
        while temp:
            if temp in nodemap:
                return True
            nodemap[temp] = 1
            temp = temp.next
        return False
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = head.next
    if detectCycle(head):
        print("Cycle detected")
    else:
        print("No cycle detected")
#optimal solution
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print("Cycle detected")
        break
    else:
        print("No cycle detected")