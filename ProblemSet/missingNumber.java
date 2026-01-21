import java.util.Scanner;
class missingNumberSolution
{
    public int missingNumber(int[] nums)
    {
        int n = nums.length;
        for(int i = 0;i<nums.length;i++)
        {
            n += i-nums[i];

        }
        return n;
    }
}
public class missingNumber
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements: ");
        for(int i = 0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        missingNumberSolution solution = new missingNumberSolution();
        int result = solution.missingNumber(nums);
        System.out.println(result);
        sc.close();
    }
}
