import java.util.Scanner;
// class Solution
// {
//     public int maximum69Number (int num) 
//     {
//         String s = Integer.toString(num);
//         char[] ch = s.toCharArray();
//         for(int i=0;i<ch.length;i++)
//         {
//             if(ch[i]=='6')
//             {
//                 ch[i]='9';
//                 break;
//             }
//         }
//         return Integer.parseInt(new String(ch));
//     }
// }
public class maximum69Number
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        int num =n;
        
        String s = Integer.toString(num);
        char[] ch = s.toCharArray();
        for(int i=0;i<ch.length;i++)
        {
            if(ch[i]=='6')
            {
                ch[i]='9';
                break;
            }
        }
        System.out.println(Integer.parseInt(new String(ch)));
        sc.close();
        
    }
}