import java.util.Scanner;
class Solution
{
    public boolean hasSameDigits(String s)
    {
       while(s.length()>2) {
        StringBuilder t=new StringBuilder();
            for(int i=0;i+1<s.length();i++)
        {
            t.append((s.charAt(i)+s.charAt(i+1))%10);
        }
            s=t.toString();
       }
       return s.charAt(0)==s.charAt(1);
    }
}
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        Solution obj=new Solution();
        boolean result=obj.hasSameDigits(s);
        System.out.println(result);
        sc.close();
    }

