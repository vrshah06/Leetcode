import java.util.Scanner;
class moveZeroesSolution 
{
    public int[] moveZeroes(int[] nums) 
    {
        int n = nums.length;
        int j = 0; // Pointer for the position of the next non-zero element
        for (int i = 0; i < n; i++) 
        {
            if (nums[i] != 0) 
            {
                nums[j++] = nums[i]; // Move non-zero element to the front
            }
        }
        while (j < n) 
        {
            nums[j++] = 0; // Fill remaining positions with zeros
        }
        return nums;
    }
}
public class moveZeros 
{
    public static void main(String[] args) 
    {
        moveZeroesSolution sol = new moveZeroesSolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int n = scanner.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < n; i++) 
        {
            nums[i] = scanner.nextInt();
        }
        scanner.close();
        int[] result = sol.moveZeroes(nums);
        System.out.print("Array after moving zeros: ");
        for (int num : result) 
        {
            System.out.print(num + " ");
        }
    }
}