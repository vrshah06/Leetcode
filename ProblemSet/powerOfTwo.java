import java.util.Scanner;
class powerOfTwoSolution
{
    public boolean isPowerOfTwo(int n)
    {
        if(n==0)
        {
            return false;
        }
        while(n!=0)
        {
            if(n==1)
            {
                return true;
            }
            if(n%2==0)
            {
                return isPowerOfTwo(n/2);
            }
            else
            {
                return false;
            }
        }
        return isPowerOfTwo(n);
    }
}
public class powerOfTwo
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        powerOfTwoSolution solution = new powerOfTwoSolution();
        boolean result = solution.isPowerOfTwo(n);
        System.out.println(result);
        sc.close();
    }
}