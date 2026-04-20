import java.util.Scanner;

class jumpGameSolution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int max = 0;
        for (int i = 0; i < n; i++) {
            if (i > max)
                return false;
            max = Math.max(max, i + nums[i]);
        }
        return true;
    }
}

public class jumpGame {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array: ");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < n; i++)
            nums[i] = sc.nextInt();
        jumpGameSolution solution = new jumpGameSolution();
        boolean result = solution.canJump(nums);
        if (result == true)
            System.out.println(result);
        else if (result == false)
            System.out.println(result);
        sc.close();
    }
}
