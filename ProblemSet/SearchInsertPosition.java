import java.util.*;
class SearchInsertPositionSolution
{
    public int searchInsert(int[] nums, int target) 
    {
        int low = 0;
        int high = nums.length - 1;
        while(low <= high)
        {
            int mid = low + (high - low) / 2;
            if(nums[mid] == target)
            {
                return mid;
            }
            else if(nums[mid] < target)
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }
        return low;
    }
}
public class SearchInsertPosition
{
    public static void main(String[] args)
    {
        SearchInsertPositionSolution s = new SearchInsertPositionSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements: ");
        int n = sc.nextInt();
        System.out.println("Enter the elements: ");
        int[] nums = new int[n];
        for(int i = 0; i < n; i++)
        {
            nums[i] = sc.nextInt();
        }
        System.out.println("Enter the target element: ");
        int target = sc.nextInt();
        System.out.println(s.searchInsert(nums, target));
        sc.close();
    }
}

/*import java.util.*;

class Solution {
    public int searchInsert(int[] nums, int target) {
        int position = 0;  // To track the insert position
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;  // Return index if found
            } else if (nums[i] < target) {
                position = i;  // Update insert position
            }
        }
        return position + 1;  // Return insert position
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int n = sc.nextInt();
        
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("Enter the target element:");
        int target = sc.nextInt();

        Solution obj = new Solution();
        int result = obj.searchInsert(arr, target);

        System.out.println("The index of the target element is: " + result);
        sc.close();
    }
}*/
