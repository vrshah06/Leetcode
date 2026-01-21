import java.util.*;
class divisionWithoutDivisionSolution
{
    public int divide(int dividend, int divisor)
    {
        int quotient = 0;
        
        if(dividend == 0)
        {
            System.out.println("Quotient is 0");
            return 0;
        }
        else if(divisor == 0)
        {
            System.out.println("Division by zero is not possible"); 
            return Integer.MAX_VALUE;
        }
        else if(dividend == Integer.MIN_VALUE && divisor == -1)
        {
            return Integer.MAX_VALUE;
        }
        else if(dividend == Integer.MIN_VALUE && divisor == 1)
        {
            return Integer.MIN_VALUE;
        }
        else if(dividend == Integer.MAX_VALUE && divisor == 1)
        {
            return Integer.MAX_VALUE;
        }
        else if(dividend == Integer.MAX_VALUE && divisor == -1)
        {
            return Integer.MIN_VALUE;
        }
        else if(dividend == Integer.MIN_VALUE && divisor == Integer.MIN_VALUE)
        {
            return 1;
        }
        else if(dividend == Integer.MAX_VALUE && divisor == Integer.MAX_VALUE)
        {
            return 1;
        }
        else if(dividend == Integer.MIN_VALUE && divisor == Integer.MAX_VALUE)
        {
            return 0;
        }
        else if(dividend == Integer.MAX_VALUE && divisor == Integer.MIN_VALUE)
        {
            return 0;
        }
        else
        {
            int sign=1;
            if(dividend<0)
            {
                dividend = -dividend;
                sign = -sign;
            }
            if(divisor<0)
            {
                divisor = -divisor;
                sign = -sign;
            }
            while(dividend>=divisor)
            {
                dividend -= divisor;
                quotient++;
        }  
        quotient = quotient * sign;

        }
        return quotient;
        
    }
}
 class divisionWithoutDivision{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the dividend: ");
        int dividend = sc.nextInt();
        System.out.println("Enter the divisor: ");
        int divisor = sc.nextInt();

        divisionWithoutDivisionSolution solution = new divisionWithoutDivisionSolution();
        int result = solution.divide(dividend, divisor);
        System.out.println("Quotient: " + result);
        sc.close();
        
}}
