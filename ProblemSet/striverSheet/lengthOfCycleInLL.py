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
            return lengthOfCycle(slow)
    return None
def lengthOfCycle(meetingPoint):
    temp = meetingPoint
    count = 0
    while temp.next != meetingPoint:
        temp = temp.next
        count += 1
    return count

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next
    cycle_length = findStartingPointOfCycle(head)
    if cycle_length:
        print("Length of cycle is:", cycle_length)
    else:
        print("No cycle detected")