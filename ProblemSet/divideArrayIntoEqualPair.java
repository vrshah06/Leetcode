import java.util.*;
class divideArrayIntoEqualPairSolution
{
    public boolean divideArray(int[] nums)
    {
        int n = nums.length;
        Arrays.sort(nums);
        for(int i = 0;i<n;i+=2)
        {
            if(nums[i]!=nums[i+1])
            {
                return false;
            }
        }
        return true;
    }
}
public class divideArrayIntoEqualPair
{
    public static void main(String[] args)
    {
        divideArrayIntoEqualPairSolution s = new divideArrayIntoEqualPairSolution();
        System.out.println("Enter the number of elements in the array");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array");
        for(int i=0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        boolean res = s.divideArray(nums);
        if(res)
        {
            System.out.println(true);
            System.out.println("The array can be divided into equal pairs");   
        }
        else
        {
            System.out.println(false);
            System.out.println("The array cannot be divided into equal pairs");
        }
        sc.close();
    }
}
