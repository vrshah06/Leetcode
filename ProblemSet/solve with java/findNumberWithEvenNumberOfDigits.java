import java.util.Scanner;
class findNumberWithEvenNumberOfDigitsSolution{
    public int findNumbers(int[] nums)
    {
        int count  = 0;
        for(int i =0;i<nums.length;i++)
        {
            int digits = 0;
            int n= nums[i];
            while(n>0)
            {
                n/=10;
                digits++;
            }
            if(digits%2==0)
            {
                count++;
            }   
        }
        return count;
    }
}
class FMain {
    public static void main(String[] args) {
        findNumberWithEvenNumberOfDigitsSolution solution = new findNumberWithEvenNumberOfDigitsSolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array:");
        int n = scanner.nextInt();
        int[] nums = new int[n];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        scanner.close();
        int result = solution.findNumbers(nums);
        System.out.println(result);
    }
}