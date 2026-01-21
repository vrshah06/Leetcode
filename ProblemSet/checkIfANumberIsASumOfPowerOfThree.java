import java.util.*;
class checkIfANumberIsASumOfPowerOfThreeSolution
{
    public boolean checkPowersOfThree(int n)
    {
         while (n>0)
         {
                if (n%3==2)
                {
                    return false;
                }
                n/=3;
         }
            return true;
    }
}
public class checkIfANumberIsASumOfPowerOfThree
{
    public static void main(String[] args)
    {
        checkIfANumberIsASumOfPowerOfThreeSolution s = new checkIfANumberIsASumOfPowerOfThreeSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number");
        int n = sc.nextInt();
        System.out.println(s.checkPowersOfThree(n));
        sc.close();
    }
}
