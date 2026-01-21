import java.util.*;
class countSubarraysOfLengthThreeSolution
{
    public int countSubarrays(int[] nums)
    {
        int count = 0;
        for(int i = 0;i<nums.length-2;i++)
        {
            if(2*(nums[i]+nums[i+2])== (nums[i+1]))
            {
                count++;
            }
        }
        return count;
    }
}
class countSubarraysOfLengthThree
{
    public static void main(String[] args)
    {
        countSubarraysOfLengthThreeSolution sol = new countSubarraysOfLengthThreeSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array: ");
        for(int i=0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        int result = sol.countSubarrays(nums);
        System.out.println("The number of subarrays of length 3 with equal sum is: " + result);
        sc.close();
    }
}
