class Solution
{
    public int canBeTypeWords(String text, String brokenLetters)
    {
        String[] words = text.split(" ");
        int count =0;
        for(String word: words)
        {
            boolean canBeTyped = true;
            for(char ch: brokenLetters.toCharArray())
            {
                if(word.indexOf(ch)!=-1)
                {
                    canBeTyped = false;
                    break;
                }
            }
            if(canBeTyped)
            {
                count++;
            }
        }
        return count;
    }
}
