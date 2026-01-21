//import java.util.*;
class convertBinaryNumberInALinkedListToIntegerSolution
{
    public int getDecimalValue(ListNode head)
    {
        int result = 0;
        ListNode current = head;
        while (current != null) {
            result = (result << 1) | current.val; // Shift left and add current value
            current = current.next; // Move to the next node
        }
        return result; // Return the final decimal value

    }
}
class ListNode {
    int val;
    ListNode next;
    
    ListNode(int x) {
        val = x;
        next = null;
    }
}
