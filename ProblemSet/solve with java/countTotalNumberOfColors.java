import java.util.*;
class countTotalNumberOfColorsSolution
{
    public long coloredCells(long n)
    {
        return 2*n*n-2*n+1;
    }
}
class countTotalNumberOfColors
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        countTotalNumberOfColorsSolution solution = new countTotalNumberOfColorsSolution();
        long result = solution.coloredCells(n);
        System.out.println(result);
        sc.close();
    }
}
