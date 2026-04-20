import java.util.*;
class countEqualAndDivisiblePairInArraySolution
{
    public int countPairs(int[] nums, int k)
    {
        int count = 0;
        for(int i = 0;i<nums.length;i++)
        {
            for(int j = i+1;j<nums.length;j++)
            {
                if(nums[i]==nums[j]&& (i*j)%k==0)
                {
                    count++;
                }
            }
        }
        return count;
    }
}
public class countEqualAndDivisiblePairInArray
{
    public static void main(String[] args)
    {
        countEqualAndDivisiblePairInArraySolution s = new countEqualAndDivisiblePairInArraySolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array:");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array:");
        for(int i = 0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        System.out.println("Enter the value of k:");
        int k = sc.nextInt();
        int result = s.countPairs(nums,k);
        System.out.println("Number of pairs: " + result);
        sc.close();
    }
}

    