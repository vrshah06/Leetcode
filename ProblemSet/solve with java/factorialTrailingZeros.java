import java.util.Scanner;
class factorialTrailingZerosSolution
{
    public int trailingZeroes(int n)
    {
        int count = 0;
        int fac = 1;
        for(int i = 0;i<=n;i++)
        {
            fac = fac * i;
        }
        while(fac%10==0)
        {
            count++;
            fac = fac/10;
        }
        return count;
    }
}
public class factorialTrailingZeros
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        factorialTrailingZerosSolution solution = new factorialTrailingZerosSolution();
        int result = solution.trailingZeroes(n);
        System.out.println(result);
        sc.close();
    }
}
// import java.util.Scanner;

// class Solution {
//     public int trailingZeroes(int n) {
//         int count = 0;
//         while (n > 0) {
//             n /= 5;
//             count += n;
//         }
//         return count;
//     }
// }

// public class FactorialTrailingZeros {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter a number: ");
//         int n = sc.nextInt();
//         Solution solution = new Solution();
//         int result = solution.trailingZeroes(n);
//         System.out.println("Number of trailing zeros in " + n + "! is: " + result);
//         sc.close();
//     }
// }
