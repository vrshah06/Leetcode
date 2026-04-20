// import java.util.Scanner;
// class Solution 
// {
//     public long squareRoot(long n) 
//     {
//         return (int)(Math.sqrt(n));
//     }}
//     public class squareRoot
//     {
//         public static void main(String[] args) 
//         {
//             Scanner sc = new Scanner(System.in);
//             long n =sc.nextLong();
//             Solution solution = new Solution();
//             System.out.println(solution.squareRoot(n));
//             sc.close();
//         }
//     }

import java.util.Scanner;

class squareRootSolution {
    public int mySqrt(long n) {  // Change parameter to long
        return (int)(Math.sqrt(n));
    }
}

public class squareRoot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();  // Read as long
        squareRootSolution solution = new squareRootSolution();
        System.out.println(solution.mySqrt(n));
        sc.close();
    }
}


   