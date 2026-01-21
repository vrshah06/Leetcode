import java.util.*;
class finalPriceDiscountSolution
{
    public int[] finalPrices(int[] prices)
    {
        int n = prices.length;
        int[] ans = new int[n];
        for(int i=0;i<n;i++)
        {
            int discount = 0;
            for(int j = i+1;j<n;j++)
            {
                if(prices[j]<=prices[i])
                {
                    discount = prices[j];
                    break;
                }
            }
            ans[i] = prices[i] - discount;
        }
        return ans;
    }
}
class finalPriceDiscount
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of prices: ");
        int n = sc.nextInt();
        int[] prices = new int[n];
        System.out.println("Enter the prices: ");
        for(int i=0;i<n;i++)
        {
            prices[i] = sc.nextInt();
        }
        finalPriceDiscountSolution solution = new finalPriceDiscountSolution();
        int[] ans = solution.finalPrices(prices);
        System.out.println("The final prices are: ");
        for(int i=0;i<n;i++)
        {
            System.out.print(ans[i]+" ");
        }
        sc.close();
    }
}