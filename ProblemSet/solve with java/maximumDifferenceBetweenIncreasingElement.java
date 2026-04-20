import java.util.*;
class maximumDifferenceBetweenIncreasingElementSolution
{
    public int maximumDifference(int[] nums)
    {
        int maxDiff = -1;
        for(int i = 0;i<nums.length;i++)
        {
            for(int j = i+1;j<nums.length;j++)
            {
                if (nums[j] > nums[i] ) {
                    maxDiff = Math.max(maxDiff, nums[j] - nums[i]);
                    
                }
            }
        }
        return maxDiff;
    }
}
public class maximumDifferenceBetweenIncreasingElement
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array:");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array:");
        for(int i = 0; i < n; i++)
        {
            nums[i] = sc.nextInt();
        }
        maximumDifferenceBetweenIncreasingElementSolution sol = new maximumDifferenceBetweenIncreasingElementSolution();
        int result = sol.maximumDifference(nums);
        if (result == -1) {
            System.out.println("No such pair exists.");
        } else {
            System.out.println("The maximum difference between increasing elements is: " + result);
        }
        sc.close();
    }
}