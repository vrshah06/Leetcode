import java.util.*;
class NumberOfOneBitsSolution
{
    public int hammingWeight(int n)
    {
            //calculate binary of the number and store it in an array
            int[] binaryNum = new int[32];
            int i = 0;
            while (n > 0) {
                binaryNum[i] = n % 2;
                n = n / 2;
                i++;
            }
            //count the number of 1's in the binary number
            int count = 0;
            for (int j = i - 1; j >= 0; j--) {
                if (binaryNum[j] == 1) {
                    count++;
                }
        }
        return count;
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number:");
        int n = sc.nextInt();
        if(n < 0)
        {
            System.out.println("Enter a positive number");
            
        }
        if(n == 0)
        {
            System.out.println("Number of 1 bits: 0");
            
        }
        NumberOfOneBitsSolution obj = new NumberOfOneBitsSolution();
        System.out.println("Number of 1 bits: " + obj.hammingWeight(n));
        sc.close();
        
    }
}
