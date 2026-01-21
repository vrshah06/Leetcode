import java.util.Scanner;
class mirrorReflectionSolution
{
    public int mirrorReflection(int p , int q)
    {
         while(p%2==0 && q%2==0)
            {
                p/=2;
                q/=2;
            }
            if(p%2==0 && q%2!=0)
            {
                return 2;
            }
            if(p%2!=0 && q%2==0)
            {
                return 0;
            }
            if(p%2!=0 && q%2!=0)
            {
                return 1;
            }
return mirrorReflection(p, q);
    }
}
public class mirrorReflection
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt();
        int q = sc.nextInt();
        mirrorReflectionSolution solution = new mirrorReflectionSolution();
        int result = solution.mirrorReflection(p, q);
        System.out.println(result);
        sc.close();
    }
}
