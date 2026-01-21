import java.util.Scanner;
class reverseIntegerSolution
{
    public int reverse(int x )
    {
        int rem,rev=0;
        boolean isNegative = x<0;
        if(isNegative)
        {
            x=-x;
        }
        while(x>0)
        {
            rem=x%10; 
            rev=rev*10+rem;
            x=x/10; 
        }
        if(rev>Integer.MAX_VALUE || rev<Integer.MIN_VALUE)
        {
            return 0;
        }
        
        return isNegative ? -rev : rev;
    }
}

public class reverseInteger
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        long n = sc.nextLong();
        reverseIntegerSolution solution = new reverseIntegerSolution();
        long result = solution.reverse((int)n);
        System.out.println(result);
        sc.close();
}
}