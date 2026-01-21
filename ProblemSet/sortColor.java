import java.util.*;
class sortColorSolution
{
    public void sortColors(int[] nums)
    {
        int zeroIndex = 0;
        int oneIndex = 0;
        int twoIndex = 0;
        for (int i = 0; i < nums.length; i++)
        {
            if (nums[i] == 0)
            {
                zeroIndex++;
            }
            else if (nums[i] == 1)
            {
                oneIndex++;
            }
            else
            {
                twoIndex++;
            }
        }
        for(int i = 0;i<nums.length;i++)
        {
            if(zeroIndex>0)
            {
                nums[i]=0;
                zeroIndex--;
            }
            else if(oneIndex>0)
            {
                nums[i]=1;
                oneIndex--;
            }
            else
            {
                nums[i]=2;
                twoIndex--;
            }
        }
    }
}
public class sortColor
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array:");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array (0, 1, or 2):");
        for (int i = 0; i < n; i++)
        {
            nums[i] = sc.nextInt();
        }
        sortColorSolution s = new sortColorSolution();
        s.sortColors(nums);
        System.out.println(Arrays.toString(nums));
        sc.close();
    }
}