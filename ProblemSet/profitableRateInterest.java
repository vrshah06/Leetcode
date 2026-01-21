import java.util.Scanner;

class profitableRateInterestSolution {
    public int profitableRateInterest(int a, int b) {
        int maxProfit = 0;
        for (int i = 0; i <= a; i++) {
            int reducedAmount = b - (2 * i);
            int leftAmount = a - i;
            if (reducedAmount > 0 && reducedAmount <= leftAmount) {
                int profitableDeposit = a - i;
                maxProfit = Math.max(maxProfit, profitableDeposit);
            }
        }
        return maxProfit;
    }
}

public final class profitableRateInterest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int testCase = 0; testCase < t; testCase++) {
            // Input: number of integers in this test case
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
        }

        //System.out.println("Enter the number of coins you have: ");
        int a = sc.nextInt();
        // minimum amount required to open profitable deposit is b coins.
        //System.out.println("Enter the minimum amount required to open profitable deposit: ");
        int b = sc.nextInt();
        profitableRateInterestSolution solution = new profitableRateInterestSolution();
        int result = solution.profitableRateInterest(a, b);
        System.out.println(result);
        sc.close();
    }
}
