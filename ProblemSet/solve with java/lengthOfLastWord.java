    import java.util.*;
    class lengthOfLastWordSolution
    {
        public int lengthOfLastWord(String s)
        {
            int count = 0;
            for(int i = 0;i<s.length();i++)
            {
                if(s.charAt(i) != ' ')
                {
                    count++;
                }
                else if(i+1<s.length() && s.charAt(i+1) != ' ')
                {
                    count = 0;
                }
            }
            return count;
        }
    }
    class lengthOfLastWord
    {
        public static void main(String[] args)
        {
            Scanner sc = new Scanner(System.in);
            String s = sc.nextLine();
            lengthOfLastWordSolution solution = new lengthOfLastWordSolution();
            int result = solution.lengthOfLastWord(s);
            System.out.println(result);
            sc.close();
        }
    }