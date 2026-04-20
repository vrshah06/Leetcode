import java.util.*;
class maximumSubarraySumSolution
{
    public int maxSubArray(int [] nums)
    {
        int maxSum = nums[0];
        for(int i = 0;i<nums.length;i++)
        {
            for(int j = i;j<nums.length;j++)
            {
                int currentSum = 0;
                for(int k = i;k<=j;k++)
                {
                    currentSum+=nums[k];
                }
                maxSum = Math.max(maxSum,currentSum);
                
            }
        }
        return maxSum;
    }
}
public class maximumSubarraySum
{
    public static void main(String[] args)
    {
        maximumSubarraySumSolution s = new maximumSubarraySumSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array: ");
        int n = sc.nextInt();
        int [] nums = new int[n];
        System.out.println("Enter the elements of the array: ");
        for(int i = 0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        int result = s.maxSubArray(nums);
        System.out.println(result);
        sc.close();
    }
}


/*
 import java.util.*;

class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0]; // Start with first element
        int currentSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter the number of elements in the array: ");
        int n = sc.nextInt();
        
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }
        
        int result = s.maxSubArray(nums);
        System.out.println("Maximum subarray sum: " + result);
        
        sc.close();
    }
}

 */