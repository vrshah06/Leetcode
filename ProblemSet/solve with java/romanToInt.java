import java.util.*;
class romanToInteger
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        //I=1, V=5, X=10, L=50, C=100, D=500, M=1000
        String s = sc.next();
        int n = s.length();
        int ans =0;
        for (int i = 0; i<n;i++)
        {
            if(s.charAt(i)=='I')
            {
                if(i+1<n && s.charAt(i+1)=='V')
                {
                    ans+=4;
                    i++;
                }
                else if(i+1<n && s.charAt(i+1)=='X')
                {
                    ans+=9;
                    i++;
                }
                else
                {
                    ans+=1;
                }
            }
            else if(s.charAt(i)=='V')
            {
                ans+=5;
            }
            else if(s.charAt(i)=='X')
            {
                if(i+1<n && s.charAt(i+1)=='L')
                {
                    ans+=40;
                    i++;
                }
                else if(i+1<n && s.charAt(i+1)=='C')
                {
                    ans+=90;
                    i++;
                }
                else
                {
                    ans+=10;
                }
            }
            else if(s.charAt(i)=='L')
            {
                ans+=50;
            }
            else if(s.charAt(i)=='C')
            {
                if(i+1<n && s.charAt(i+1)=='D')
                {
                    ans+=400;
                    i++;
                }
                else if(i+1<n && s.charAt(i+1)=='M')
                {
                    ans+=900;
                    i++;
                }
                else
                {
                    ans+=100;
                }

            }
        else if(s.charAt(i)=='D')
        {
            ans+=500;
        }
        else if(s.charAt(i)=='M')
        {
            ans+=1000;
        }
    }
    System.out.println(ans);
    sc.close();
}
}
