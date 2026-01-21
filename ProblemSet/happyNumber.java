import java.util.Scanner;

class happyNumberSolution {
    public boolean isHappy(int n) {
        if (n == 1) {
            return true;
        }
        if (n == 4) {
            return false;
        }
        int sum = 0;
        while (n != 0) {
            sum = sum + (int) (Math.pow(n % 10, 2));
            n = n / 10;
        }
        return isHappy(sum);
    }
}

public class happyNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        happyNumberSolution solution = new happyNumberSolution();
        boolean result = solution.isHappy(n);
        System.out.println(result);
        sc.close();
    }
}