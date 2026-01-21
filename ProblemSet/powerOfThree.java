import java.util.Scanner;
class powerOfThreeSolution
{
    public boolean isPowerOfThree(int n)
    {
        if(n<=0)
        {
            return false;
        }
        if(n==1)
        {
            return true;
        }
        while(n%3==0)
        {
            return isPowerOfThree(n/3);
        }
        return false;
    }
}
public class powerOfThree
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        powerOfThreeSolution solution = new powerOfThreeSolution();
        boolean result = solution.isPowerOfThree(n);
        System.out.println(result);
        sc.close();
    }
}