import java.util.*;
class NumberSmallerThanTheCurrentNumbersSolution
{
    public int[] smallerNumbersThanCurrent(int[] nums) 
    {
                int numsSize = nums.length;
                int[] result = new int[numsSize];
                for (int i = 0; i < numsSize; i++) {
                    int count = 0;
                    for (int j = 0; j < numsSize; j++) {
                        if (nums[j] < nums[i]) {
                            count++;
                        }
                    }
                    result[i] = count;
                }
                return result;
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array:");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array:");
        for(int i=0;i<n;i++)
        {
            arr[i] = sc.nextInt();
        }
        NumberSmallerThanTheCurrentNumbersSolution obj = new NumberSmallerThanTheCurrentNumbersSolution();
        int[] result = obj.smallerNumbersThanCurrent(arr);
        System.out.println("The number of elements smaller than the current element are:");
        for(int i=0;i<result.length;i++)
        {
            System.out.print(result[i]+" ");
        }
        sc.close();
    }
}
