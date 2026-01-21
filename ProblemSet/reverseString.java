import java.util.*;
class reverseStringSolution
{
    public void reverseString(char[] s)
    {
        int i = 0;
        int j = s.length-1;
        while (i<j)
        {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }
    }
}
class reverseString
{
    public static void main(String[] args)
    {
        reverseStringSolution solution = new reverseStringSolution();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string");
        String str = sc.nextLine();
        char[] s = str.toCharArray();
        solution.reverseString(s);
        System.out.println(s);
        sc.close();
    }
}