import java.util.Scanner;
class countGoodTripletsSolution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        int n = arr.length;
        int count = 0;
        for(int i = 0;i<n;i++)
        {
            for(int j = i+1;j<n;j++)
            {
                for(int k = j+1;k<n;k++)
                {
                    if(Math.abs(arr[i]-arr[j]) <= a && Math.abs(arr[j]-arr[k]) <= b && Math.abs(arr[i]-arr[k]) <= c)
                    {
                        count++;
                    }
                }
            }
        }
        return count;
        
    }
}
class countGoodTriplets {
    public static void main(String[] args) {
        countGoodTripletsSolution sol = new countGoodTripletsSolution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        System.out.println("Enter the values of a, b, c: ");
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        scanner.close();
        int result = sol.countGoodTriplets(arr, a, b, c);
        System.out.println("Number of good triplets: " + result);
    }
}