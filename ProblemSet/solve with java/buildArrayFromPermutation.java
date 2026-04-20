import java.util.*;
class buildArrayFromPermutationSolution
{
    public int[] buildArray(int[] nums)
    {
        int n = nums.length;
        int[] ans = new int[n];
        for(int i = 0;i<n;i++)
        {
            ans[i] = nums[nums[i]];
        }
        return ans;
    }
}
class buildArrayFromPermutation
{
    public static void main(String[] args)
    {
        buildArrayFromPermutationSolution solution = new buildArrayFromPermutationSolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array: ");
        for(int i = 0;i<n;i++)
        {
            nums[i] = scanner.nextInt();
        }
        scanner.close();
        int[] result = solution.buildArray(nums);
        System.out.println("The resulting array is: ");
        System.out.println(Arrays.toString(result));
    }
}