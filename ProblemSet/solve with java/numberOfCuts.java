import java.util.Scanner;
class numberOfCutsSolution
{
    public int numberOfCuts(int n)
    {
        if(n==1)
        {
            return 0;
        }
        else if(n%2==0)
        {
            return n/2;
        }
        else
        {
            return n;
        }
    }
}
public class numberOfCuts
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        numberOfCutsSolution solution = new numberOfCutsSolution();
        int result = solution.numberOfCuts(n);
        System.out.println(result);
        sc.close();
    }
}
