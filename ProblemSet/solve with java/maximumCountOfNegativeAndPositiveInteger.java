import java.util.*;
class maximumCountOfNegativeAndPositiveIntegerSolution
{
    public int maximumCount(int[] nums)
    {
        int pos = 0;
        int neg = 0;
        for(int i = 0;i<nums.length;i++)
        {
            if(nums[i]>0)
            {
                pos++;
            }
            else if(nums[i]<0)
            {
                neg++;
            }
            else if(nums[i]==0)
            {
                continue;
            }
        }
        if(pos>neg)
        {
            return pos;
        }
        else
        {
            return neg;
        }
    }
}
class maximumCountOfNegativeAndPositiveInteger
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for(int i = 0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        maximumCountOfNegativeAndPositiveIntegerSolution solution = new maximumCountOfNegativeAndPositiveIntegerSolution();
        int result = solution.maximumCount(nums);
        System.out.println(result);
        sc.close();
    }
}
