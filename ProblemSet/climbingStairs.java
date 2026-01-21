import java.util.Scanner;

class climbStairsSolution {
    public int climbStairs(int n) {  
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}

 class ClimbingStairs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        climbStairsSolution solution = new climbStairsSolution();
        int result = solution.climbStairs(n);  
        System.out.println(result);
        sc.close();
    }
}

// import java.util.Scanner;
// class ClimbingStairs {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int n = sc.nextInt();
//         if (n == 1) {
//             System.out.print(1);
//         }
//         int[] dp = new int[n + 1];
//         dp[1] = 1;
//         dp[2] = 2;
//         for (int i = 3; i <= n; i++) {
//             dp[i] = dp[i - 1] + dp[i - 2];
//         }
//         System.out.println(dp[n]);
//         sc.close();
//     }
// }


        