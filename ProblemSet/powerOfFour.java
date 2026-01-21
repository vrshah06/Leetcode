import java.util.Scanner;
class powerOfFourSolution
{
    public boolean isPowerOfFour(int n)
    {
        if(n==0)
        {
            return false;
        }
        while (n!=0) {
            if(n==1)
            {
                return true;
            }
            if(n%4==0)
            {  
                return isPowerOfFour(n/4); 
            }
            else
            {
                return false;
            }
        }
        return isPowerOfFour(n);
    }
}
public class powerOfFour
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        powerOfFourSolution solution = new powerOfFourSolution();
        boolean result = solution.isPowerOfFour(n);
        System.out.println(result);
        sc.close();
    }
}