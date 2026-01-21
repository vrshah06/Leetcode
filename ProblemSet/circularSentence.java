import java.util.Scanner;
class circularSentenceSolution
{
    public boolean isCircular(String s)
    {
        int n = s.length();
        if(s.charAt(0)!=s.charAt(n-1)){
            return false;
        }
        for(int i =1; i<n-1; i++)
        {
            if(s.charAt(i)==' ')
            {
                if(s.charAt(i-1)!=s.charAt(i+1))
                {
                    return false;
                }
                
            }
        }
        return true;
    }
}
public class circularSentence
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String s = sc.nextLine();
        circularSentenceSolution solution = new circularSentenceSolution();
        boolean result = solution.isCircular(s);
        System.out.println(result);
        sc.close();
    }
}