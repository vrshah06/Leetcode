import java.util.*;
class threeConsecutiveOddsSolution
{
    public boolean threeConsecutiveOdds(int[] arr)
    {
        int count  = 0;
        for(int i = 0;i<arr.length;i++)
        {
            if(arr[i]%2==0)
            {
                count = 0;
            }
            else
            {
                count++;
                if(count == 3)
                {
                    return true;
                }
            }
        } 
        return false;
 }
}
class threeConsecutiveOdds
{
    public static void main(String[] args)
    {
        threeConsecutiveOddsSolution solution = new threeConsecutiveOddsSolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array: ");
        for(int i = 0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        scanner.close();
        boolean result = solution.threeConsecutiveOdds(arr);
        System.out.println("The result is: " + result);
    }
}
