class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#optimal solution
def findStartingPointOfCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = head.next
    starting_point = findStartingPointOfCycle(head)
    if starting_point:
        print("Starting point of cycle is:", starting_point.data)
    else:
        print("No cycle detected")