import java.util.*;

class countLargestGroupSolution {
    public int countLargestGroup(int n) {
       
        int[] sumcount = new int[37]; // index 0 won't be used
        
        // Calculate digit sum for each number and count frequencies
        for (int i = 1; i <= n; i++) {
            int sum = digitSum(i);
            sumcount[sum]++;
        }
        
        // Find the maximum group size
        int maxSize = 0;
        for (int count : sumcount) {
            if (count > maxSize) {
                maxSize = count;
            }
        }
        
        // Count how many groups have this maximum size
        int result = 0;
        for (int count : sumcount) {
            if (count == maxSize) {
                result++;
            }
        }
        
        return result;
    }
    
    private int digitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

public class countLargestGroup {
    public static void main(String[] args) {
        countLargestGroupSolution s = new countLargestGroupSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n = sc.nextInt();
        int result = s.countLargestGroup(n);
        System.out.println("The number of groups with the largest size is: " + result);
        sc.close();

    }
}

//Python approach
/*
n = int(input("Enter the number: "))
num=[0]*1000
max=0
for i in range(1,n+1):
    sum = 0
    temp=i
    while temp>0:
        sum+=temp%10
        temp//=10
    num[sum]+=1
for count in num:
    if count>max:
        max=count
group=0
for count in num:
    if count==max:
        group+=1
*/
