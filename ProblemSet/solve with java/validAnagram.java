import java.util.*;
class validAnagramSolution
{
    public boolean isAnagram(String s,String t)
    {
        if(s.length()==t.length())
        {
            char[] s1 = s.toCharArray();
            char[] t1 = t.toCharArray();
            Arrays.sort(s1);
            Arrays.sort(t1);
            for(int i = 0;i<s1.length;i++)
            {
                if(s1[i]!=t1[i])
                {
                    return false;
                }
            }
            return true;
        }
        else
        {
            return false;
        }
    }
}
class validAnagram
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string 1:");
        String s = sc.nextLine();
        System.out.println("Enter string 2:");
        String t = sc.nextLine();
        validAnagramSolution solution = new validAnagramSolution();
        boolean result = solution.isAnagram(s,t);
        System.out.println(result);
        sc.close();
    }
}
