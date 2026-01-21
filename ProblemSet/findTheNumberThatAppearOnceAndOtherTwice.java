import java.util.*;
class findNumberThatAppearOnceSolution
{
    public int[] findNumberThatAppearOnce(int[] nums)
    {
        int currentCount = 0;
        int count = 0;
        for(int i = 0;i<nums.length;i++)
        {
            currentCount = 0;
            for(int j = 0;j<nums.length;j++)
            {
                if(nums[i] == nums[j])
                {
                    currentCount++;
                }
            }
            if(currentCount == 1)
            {
                return new int[]{nums[i]} ;
            }
        }
        return new int[]{-1};
    }
}
public class findTheNumberThatAppearOnceAndOtherTwice
{
    public static void main(String[] args)
    {
        findNumberThatAppearOnceSolution solution = new findNumberThatAppearOnceSolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array:");
        int n = scanner.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array:");
        for(int i = 0; i < n; i++)
        {
            nums[i] = scanner.nextInt();
        }
        System.out.println("The number that appears once is:");
        int[] result = solution.findNumberThatAppearOnce(nums);
        System.out.println(Arrays.toString(result));
        scanner.close();
    }
}