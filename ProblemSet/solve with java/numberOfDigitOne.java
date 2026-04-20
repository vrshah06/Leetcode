import java.util.Scanner;
class numberOfDigitOneSolution
{
    public int countDigitOne(int n)
    {
        int count = 0;
        for(long i = 1;i<=n;i++)
        {
            long temp = i;
            while (temp>0)
             {
                if(temp%10==1)
                {
                    count++;
                }
                temp = temp/10;
            }

        }
        return count;
    }
}
public class numberOfDigitOne
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt();
        numberOfDigitOneSolution solution = new numberOfDigitOneSolution();
        int result = solution.countDigitOne(n);
        System.out.println(result);
        sc.close();
    }
}