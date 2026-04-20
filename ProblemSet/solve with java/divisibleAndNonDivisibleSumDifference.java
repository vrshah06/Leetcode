import java.util.*;
class divisibleAndNonDivisibleSumDifferenceSolution
{
    public int differenceOfSums(int n, int m)
    {
        int divisibleSum = 0;
        int nonDivisibleSum = 0;
        for(int i = 0;i<=n;i++)
        {
            if(i%m==0)
            {
                divisibleSum += i;
            }
            else
            {
                nonDivisibleSum += i;
            }
        }
        int differenceOfSums = nonDivisibleSum - divisibleSum;
        return differenceOfSums;
    }
}
class DMain
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of n:");
        int n = sc.nextInt();
        System.out.println("Enter the value of m:");
        int m = sc.nextInt();

        divisibleAndNonDivisibleSumDifferenceSolution solution = new divisibleAndNonDivisibleSumDifferenceSolution();
        int result = solution.differenceOfSums(n, m);
        
        System.out.println("The difference of sums is: " + result);
        sc.close();
    }
}