import java.util.*;
class arrangeCoinsSolution
{
    public int arrangeCoins(int n)
    {
        int count = 0;
        for(int i = 1;i<=n;i++)
        {
            n=n-i;
            count++;
        }
        return count;
    }
}
class arrangeCoins
{
    public  static void main(String[] args)
    {
        Scanner sc = new Scanner (System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        arrangeCoinsSolution solution = new arrangeCoinsSolution();
        int result = solution.arrangeCoins(n);
        System.out.println("Number of coins that can be arranged in staircase pattern is: " + result);
        sc.close();
    }
}
