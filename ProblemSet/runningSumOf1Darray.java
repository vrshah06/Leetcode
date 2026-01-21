import java.util.*;
class runningSumSolution
{
    public int[] runningSum(int[] nums)
    {
        int n = nums.length;
        int[] res = new int[n];
        res[0]=nums[0];
        for(int i=1;i<n;i++)
        {
            res[i]= res[i-1]+nums[i];
        }
        return res;
    }
}
public class runningSumOf1Darray
{
    public static void main(String[] args)
    {
        runningSumSolution s = new runningSumSolution();
        System.out.println("Enter the number of elements in the array");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array");
        for(int i=0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        int[] res = s.runningSum(nums);
        for(int i=0;i<res.length;i++)
        {
            System.out.print(res[i]+" ");
        }
        sc.close();
    }
}
