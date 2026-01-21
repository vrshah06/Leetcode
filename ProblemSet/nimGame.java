import java.util.Scanner;
class nimGameSolution
{
    public boolean canWinNim(int n)
    {
        if(n%4==0)
        {
            return false;
        }
        return true;
    }
}
public class nimGame
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of stones: ");
        int n = sc.nextInt();
        nimGameSolution solution = new nimGameSolution();
        boolean result = solution.canWinNim(n);
        System.out.println(result);
        sc.close();
    }
}