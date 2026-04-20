import java.util.Scanner;
class sumOfTwoIntegersSolution
{
    public int getSum(int a, int b)
    {
        while(b != 0)
        {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
}
public class sumOfTwoIntegers
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers: ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        sumOfTwoIntegersSolution solution = new sumOfTwoIntegersSolution();
        int result = solution.getSum(a, b);
        System.out.println(result);
        sc.close();
    }
}