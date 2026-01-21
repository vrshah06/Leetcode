import java.util.Scanner;
class checkIfExistSolution
{
    public boolean checkIfExist(int[] arr)
    {
        for(int i = 0; i<arr.length;i++)
        {
            for(int j = 0; j<arr.length;j++)
            {
                if(i!=j && arr[i]==2*arr[j])
                {
                    return true;
                }
            }
        }
        return false;
    }
}
class checkIfExist
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i<n; i++)
        {
            arr[i] = sc.nextInt();
        }
        checkIfExistSolution solution = new checkIfExistSolution();
        boolean result = solution.checkIfExist(arr);
        System.out.println(result);
        sc.close();
    }
}
