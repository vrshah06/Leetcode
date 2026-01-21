 import java.util.Scanner;
// class power
// {
//     public static void main(String[] args)
//     {
//         Scanner sc = new Scanner(System.in);
//         System.out.println("Enter the base number: ");
//         double base = sc.nextDouble();
//         System.out.println("Enter the power: ");
//         int power = sc.nextInt();
//         if(power == 0)
//         {
//             System.out.println("The result is 1");
//         }
//         else if(base == 0)
//         {
//             System.out.println("The result is 0");
//         }
//         else
//         {
//             System.out.println("The result is: " + (double)(Math.pow(base, power)));
//         }
//         sc.close();

//     }
// }


class powerSolution
{
    public double myPow(double x , int n)
    {
        if(n == 0)
        {
            return 1;
        }
        else if(x == 0)
        {
            return 0;
        }
        else
        {
            return (double)(Math.pow(x, n));
        }
    }
}
class power
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the base number: ");
        double x = sc.nextDouble();
        System.out.println("Enter the power: ");
        int n = sc.nextInt();
        powerSolution solution = new powerSolution();
        double result = solution.myPow(x, n);
        System.out.println("The result is: " + result);
        sc.close();
    }
}