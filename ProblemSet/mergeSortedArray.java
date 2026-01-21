import java.util.*;
class mergeSortedArraySolution
{
    public void merge(int[] nums1,int m, int[] nums2,int n)
    {
        for(int j = 0,i=m;j<n;j++)
        {
            nums1[i]=nums2[j];
            i++;
        }
        Arrays.sort(nums1);
        
    }
}
class mergeSortedArray
{
    public static void main(String[] args)
    {
        mergeSortedArraySolution s = new mergeSortedArraySolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of first array: ");
        int m = sc.nextInt();
        System.out.println("Enter the size of second array: ");
        int n = sc.nextInt();
        int[] nums1 = new int[m+n];
        int[] nums2 = new int[n];
        System.out.println("Enter the elements of first array: ");
        for(int i=0;i<m;i++)
        {
            nums1[i] = sc.nextInt();
        }
        System.out.println("Enter the elements of second array: ");
        for(int i=0;i<n;i++)
        {
            nums2[i] = sc.nextInt();
        }
        System.out.println("The merged array is: ");
        s.merge(nums1,m,nums2,n);
        for(int i=0;i<m+n;i++)
        {
            System.out.print(nums1[i]+" ");
        }
        System.out.println();
        sc.close();
    }
}