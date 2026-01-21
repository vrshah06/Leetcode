import java.util.*;
class maximumValueOfOrderedTripletSolution
{
    public long maximumTripletValue(int[] arr)
    {
        int n = arr.length;
        int max = 0;
        int diff = 0;
        long res = 0;
        for(int i = 0;i<n;i++)
        {
            max= Math.max(max,arr[i]);
            if(i>=2)
            {
                res = Math.max(res,(long)diff*arr[i]);
            }
            if(i>=1)
            {
                diff = Math.max(diff,max-arr[i]);
            }
        }
        return res;
    }
}
public class maximumValueOfOrderedTriplet
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();   
        int [] arr = new int[n];
        for(int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }
        maximumValueOfOrderedTripletSolution obj = new maximumValueOfOrderedTripletSolution();
        long ans = obj.maximumTripletValue(arr);
        System.out.println(ans);
        sc.close();
    }
}