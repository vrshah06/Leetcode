import java.util.Scanner;

class integerReplacementSolution {
    public int integerReplacement(int n) {
        int operations = 0;
        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                 if(n==Integer.MAX_VALUE)
                {
                    n= n/2 + 1;
                }
                else if (n == 3) {
                    n--;
                } else if ((n + 1) % 4 == 0) {
                    n++;
                } 
                
                else {
                    n--;
                }
            }
            operations++;
        }
        return operations;
    }
}

public class integerReplacement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        integerReplacementSolution solution = new integerReplacementSolution();
        int result = solution.integerReplacement(n);
        System.out.println(result);
        sc.close();
    }
}