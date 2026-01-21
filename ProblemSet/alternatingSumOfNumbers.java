import java.util.Scanner;

class  alternatingSumOfNumbersSolution {
    public int alternatingSumOfNumbers(int n, int[] arr) {

        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                sum += arr[i];
                sum -= arr[i];
            }
        }
        return sum;
    }
}

public final class alternatingSumOfNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        // Loop through each test case
        for (int testCase = 0; testCase < t; testCase++) {
            // Input: number of integers in this test case
            int n = sc.nextInt();
            int[] arr = new int[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        alternatingSumOfNumbersSolution solution = new alternatingSumOfNumbersSolution();
        int result = solution.alternatingSumOfNumbers(n, arr);
        System.out.println(result);
        
    }
    sc.close();
}}