//import java.util.*;
/*public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class ListNodeSolution{
    public ListNode deleteMiddle(ListNode head)
    {
        if(head==null || head.next == null)
        {
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;   
        ListNode prev = null; // To keep track of the previous node
        while (fast != null && fast.next!=null) {
            prev = slow;
            slow = slow.next; // Move slow by 1 step
            fast = fast.next.next; // Move fast by 2 steps        
        }
        slow = slow.next; // Move slow to the next node
        if (prev != null) {
            prev.next = slow; // Link the previous node to the next of slow
        } else {
            head = slow; // If prev is null, it means we are deleting the head
        }
        return head; // Return the modified list
    }
}