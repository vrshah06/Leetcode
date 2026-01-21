//import java.util.*;
class reversedLinkedListSolution
{
    public ListNode reverseList(ListNode head)
    {
         if (head==null || head.next==null)
          {
            return head;
         }
         ListNode prev =null;
         ListNode curr= head;
            ListNode next = null;
            while (curr!=null)
            {
                next = curr.next;// Store the next node
                curr.next = prev;// Reverse the current node's pointer
                prev = curr;// Move prev to the current node
                curr =next;// Move to the next node
                
            }
            return prev;
    }
}