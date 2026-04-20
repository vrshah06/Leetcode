import java.util.*;
class largestPerimeterTriangleSolution
{
    public int largestPerimeter(int[] nums)
    {
        Arrays.sort(nums);
        for(int i = nums.length - 1;i>=2;i--)
        {
            if(nums[i]<nums[i-1]+nums[i-2])
            {
                return nums[i]+nums[i-1]+nums[i-2];
            }
        }
        return 0;
    }
}
class largestPerimeterTriangle
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
        largestPerimeterTriangleSolution solution = new largestPerimeterTriangleSolution();
        int result = solution.largestPerimeter(nums);
        System.out.println(result);
        sc.close();
        
    }
}
