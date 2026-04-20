import java.util.*;
class typeOfTriangleSolution
{
    public String triangleType (int [] nums)
    {
        int a  =nums[0];        
        int b  =nums[1];
        int c  =nums[2];
        if(a+b>c && a+c>b && b+c>a)
        {
            if(a==b && b==c)
            {
                return "Equilateral";
            }
            else if(a==b || b==c || a==c)
            {
                return "Isosceles";
            }
            else
            {
                return "Scalene";
            }
        }
        else
        {
            return "Not a triangle";
        }
    }
}
class typeOfTriangle
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the three sides of the triangle:");
        int [] nums = new int[3];
        for (int i = 0; i < 3; i++)
        {
            nums[i] = sc.nextInt();
        }
        typeOfTriangleSolution s = new typeOfTriangleSolution();
        String result = s.triangleType(nums);
        System.out.println(result);
        sc.close();
    }
}