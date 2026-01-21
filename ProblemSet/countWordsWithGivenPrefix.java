import java.util.*;
class countWordsWithGivenPrefixSolution
{
    public int prefixCount(String[] words,String pref)
    {
        int count = 0;
        for(int i=0;i<words.length;i++)
        {
            if(words[i].startsWith(pref))
            {
                count++;
            }
            else
            {
                continue;
            }
        }
        return count;
    }
}
class countWordsWithGivenPrefix
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of words: ");
        int n =sc.nextInt();
        String[] words = new String[n];
        System.out.println("Enter the words: ");
        for(int i=0;i<n;i++)
        {
            words[i] = sc.next();
        }
        System.out.println("Enter the prefix: ");
        String pref = sc.next();
        countWordsWithGivenPrefixSolution solution = new countWordsWithGivenPrefixSolution();
        int result = solution.prefixCount(words,pref);
        System.out.println(result);
        sc.close();
    }
}