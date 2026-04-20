import java.util.Scanner;
class addDigitsSolution
{
    public int addDigits(int num)
    {
        int temp = num;
        if(num<10 && num>=0)
        {
            return num;
        }
        int sum= 0;
        while(temp>0)
         {
            sum+=temp%10;
            temp=temp/10;
         }
        return addDigits(sum);
    }
}
public class addDigit
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        addDigitsSolution solution = new addDigitsSolution();
        int result = solution.addDigits(num);
        System.out.println(result);
        sc.close();
    }
}