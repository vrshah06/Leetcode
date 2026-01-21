import java.util.*;
class superPowerSolution
{
    public int superPow(double  a , double[] b)
    {
        int n = b.length;
         double ans = 1;
         for(int i = 0;i<n;i++)
         {
                ans = Math.pow(ans,10)*Math.pow(a,b[i])%1337;
         }
            return (int)ans;
    }
}
public class superPower
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        int n = sc.nextInt();
        double [] b = new double[n];
        for(int i = 0;i<n;i++)
        {
            b[i] = sc.nextInt();
        }
        superPowerSolution obj = new superPowerSolution();
       double res = obj.superPow(a,b);
        System.out.println(res);
        sc.close();
    }
}