import java.util.*;
class calculateSeries
{
    public int seriesType(int n)
    {
        if(n==0)
        {
            return 0;
        }
        else if(n==1)
        {
            return 1;
        }
        else if (n==2)
        {
            return 2;
        }
        else if (n==3)
        {
            return 3;
        }
        else if(n==4)
        {
            return 4;
        }
        else if(n==5)
        {
            return 10;
        }
        else{
            return 2 * seriesType(n-1);
        }     
    }
}
public class calculateSeriesMain
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of n:");
        int n =sc.nextInt();
        calculateSeries solution = new calculateSeries();
        int result = solution.seriesType(n);
        System.out.println(result);
        sc.close();
    }
}
