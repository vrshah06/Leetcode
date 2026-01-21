import java.util.Scanner;

class maximumMatrixSumSolution {
    public long maxMatrixSum(int[][] matrix) {

        long ans = 0;
        int negCount = 0;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] < 0) {
                    negCount++;
                }
                ans += Math.abs(matrix[i][j]);
                if (min > Math.abs(matrix[i][j]))
                    min = Math.abs(matrix[i][j]);
            }
        }
        if (negCount % 2 == 0)
            return ans;
        else {
            return ans - 2 * min;
        }
    }
}

public class maximumMatrixSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows: ");
        int n = sc.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        maximumMatrixSumSolution solution = new maximumMatrixSumSolution();
        long result = solution.maxMatrixSum(matrix);
        System.out.println(result);
        sc.close();
    }
}