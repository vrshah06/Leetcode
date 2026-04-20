import java.util.*;
class maxConsecutiveOnesSolution
{
    public int findMaxConsecutiveOnes(int[] nums)
    {
        int maxCount =0 ;
        int currentCount =0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==1)
            {
                currentCount++;
            }
            else
            {
                maxCount = Math.max(maxCount,currentCount);
                currentCount = 0;   
            }
        }
        maxCount = Math.max(maxCount,currentCount);
        return maxCount;
    }
}
class maxConsecutiveOnes
{
    public static void main(String[] args)
    {
        maxConsecutiveOnesSolution sol = new maxConsecutiveOnesSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array: ");
        for(int i=0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        int result = sol.findMaxConsecutiveOnes(nums);
        System.out.println("The maximum number of consecutive 1's is: " + result);
        sc.close();

    }
}