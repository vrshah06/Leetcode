import java.util.Scanner;
class uglyNumberSolution
{
    public boolean isUgly(int n)
    {
        if(n<=0)
        {
            return false;
        }
        if(n==1)
        {
            return true;
        }
        while (n%2==0)
        {
            n = n/2;
        }
        while (n%3==0)
        {
            n = n/3;
        }
        while (n%5==0)
        {
            n = n/5;
        }
        return n==1;
    }
}
public class uglyNumber
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        uglyNumberSolution solution = new uglyNumberSolution();
        boolean result = solution.isUgly(n);
        System.out.println(result);
        sc.close();
    }
}