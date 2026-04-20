import java.util.*;
class countNumbersWithUniqueDigitsSolution
{
     
        public int countNumbersWithUniqueDigits(int n) {
            if (n == 0) {
                return 1;
            }
            int total = 10;
            int prod = 9;
            for (int i = 2; i < n + 1; i++) {
                total += prod * (11 - i);
                prod *= 11 - i;
            }
            return total;
        }
    
}
public class countNumberWithUniqueDigits
{
    public static void main(String[] args)
    {
        countNumbersWithUniqueDigitsSolution s = new countNumbersWithUniqueDigitsSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of digits: ");
        int n = sc.nextInt();
        int result = s.countNumbersWithUniqueDigits(n);
        System.out.println(result);
        sc.close();
    }
}