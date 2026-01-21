import java.util.*;
class rearrangeArraySolution
{
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] positives = new int[n/2];
        int[] negatives = new int[n/2];
        int posIndex = 0, negIndex =0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                positives[posIndex++] = nums[i];
                
            } else {
                negatives[negIndex++] = nums[i];
            }
        }
        int[] result = new int[n];
        int pos = 0;
        int neg = 0;
        boolean flag = true;
        for(int i = 0;i<n;i++)
        {
            if (flag) {
                result[i] = positives[pos++];
            } else {
                result[i] = negatives[neg++];
                
            }
            flag = !flag;
        }
        return result;
}
}
class RMain {
    public static void main(String[] args) {
        rearrangeArraySolution solution = new rearrangeArraySolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array:");
        int n = scanner.nextInt();
        int[] nums = new int[n];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        scanner.close();
        int[] result = solution.rearrangeArray(nums);
        System.out.println(Arrays.toString(result));
    }
}