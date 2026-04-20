import java.util.*;
class StringLenthAfterTransformationSolution
{
    public int lengthAfterTransformation(String s,int t)
    {
        long n = s.length();
        
        for(int i = 0; i < t; i++)
        {
            long newLength = 0;
            StringBuilder sb = new StringBuilder();
            
            for (int j = 0; j < n; j++)
            {
                char c = s.charAt(j);
                   if (s.charAt(j)=='z') {
                    sb.append("ab");
                    newLength += 2;
                    
                }
                 else {
                    sb.append((char)(c + 1));
                    newLength += 1;
                }
              
            }
            s = sb.toString();
            n = newLength;
        }
        return (int)n;
}
}
public class StringLenthAfterTransformation
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String: ");
        String s = sc.nextLine();
        System.out.println("Enter the number of transformations: ");
        int t = sc.nextInt();
        StringLenthAfterTransformationSolution obj = new StringLenthAfterTransformationSolution();
        int result = obj.lengthAfterTransformation(s, t);
        sc.close();
        System.out.println("The length of the string after " + t + " transformations is: " + result);
    }

}
