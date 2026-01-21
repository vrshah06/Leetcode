import java.util.*;
class maximumSumOfArrayAfterKNegationsSolution
{
    public int largestSumAfterKNegations(int[] nums, int k)
    {
        Arrays.sort(nums);
        for(int i = 0;i<nums.length;i++)
        {
            if(k>0 && nums[i]<0)
            {
                nums[i] = -nums[i];
                k--;
            }
        }
        Arrays.sort(nums);
        if(k%2!=0)
        {
            nums[0] = -nums[0];
        }
        int sum = 0;
        for(int i = 0;i<nums.length;i++)
        {
            sum+=nums[i];
        }
        return sum;
    }
}
public class maximumSumOfArrayAfterKNegations
{
    public static void main(String[] args)
    {
        maximumSumOfArrayAfterKNegationsSolution s = new maximumSumOfArrayAfterKNegationsSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array");
        for(int i = 0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        System.out.println("Enter the value of k");
        int k = sc.nextInt();
        System.out.println(s.largestSumAfterKNegations(nums,k));
        sc.close();
    }
}