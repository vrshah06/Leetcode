import java.util.*;

class singleNumberSolution {
    public int singleNumber(int[] nums) {
        int result = 0;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }
            if (count == 1) {
                result = nums[i];
                break;
            } else {
                count = 0;
            }
            
        }
        return result;
    }
}

public class singleNumber {
    public static void main(String[] args) {
        singleNumberSolution s = new singleNumberSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter the elements of the array");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }
        System.out.println(s.singleNumber(nums));
        sc.close();
    }
}