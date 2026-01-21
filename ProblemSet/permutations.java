import java.util.*;
class permutationsSolution
{
    public int permute(int[] nums)
    {
        int n = nums.length;
        //n factorial
        int fact = 1;
       // int count = 0;
        Arrays.sort(nums);
        if(n==0)
        {
            return 1;
        }
        // in a array of n elements how many elements are repeated
        // for(int i = 0;i<n-1;i++)
        // {
        //     if(nums[i]==nums[i+1])
        //     {
        //         count++;
        //     }
        //     //divide n factorial by the factorial of the repeated elements
        //     fact = fact/(count+1);
        //     count = 0;
        // }
        // if there are no repeated elements
        for(int i = 1;i<=n;i++)
        {
            fact = fact*i;
        }
        return fact;
    }
}
class permutations
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array");
        int n = sc.nextInt();
        System.out.println("Enter the elements of the array");
        int[] nums = new int[n];
        for(int i = 0;i<n;i++)
        {
            nums[i] = sc.nextInt();
        }
        permutationsSolution solution = new permutationsSolution();
        int result = solution.permute(nums);
        System.out.println(result);
        sc.close();
    }
}
