import java.util.*;
class fibonacciNumberSolution
{
    public int fib(int n)
    {
        if(n==0)
        {
            return 0;
        }
        if(n==1)
        {
            return 1;
        }
        if(n>1)
        {
            return fib(n-1) + fib(n-2);
        }
        return 0;
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number  ");
        int n=sc.nextInt();
        fibonacciNumberSolution s=new fibonacciNumberSolution();
        int result=s.fib(n);
        System.out.println(result);
        sc.close();
        

    }
}