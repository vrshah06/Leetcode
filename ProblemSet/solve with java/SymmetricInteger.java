import java.util.*;
class SymmetricIntegerSolution
{
    public int countSymmetricIntegers(int low, int high) 
    {
         if(low > high) return 0;
         int count = 0;
         for(int i = low; i <= high; i++)
         {
                String s = Integer.toString(i);
                int n = s.length();
                if(n % 2 == 0)
                {
                    int left = 0, right = 0;
                    for(int j =0;j<n/2;j++)
                    {
                        left += s.charAt(j) - '0';
                        right += s.charAt(n-j-1) - '0';
                    }
                    if(left == right) count++;
                    
                }
    
    }
    return count;
}
}
public class SymmetricInteger
{
    public static void main(String[] args) {
        SymmetricIntegerSolution sol = new SymmetricIntegerSolution();
        System.out.println("Enter the range of integers (low and high): ");
        Scanner scanner = new Scanner(System.in);
        int low = scanner.nextInt();
        int high = scanner.nextInt();
        scanner.close();
        int result = sol.countSymmetricIntegers(low, high);
        System.out.println("Count of symmetric integers between " + low + " and " + high + " is: " + result);
    }
}