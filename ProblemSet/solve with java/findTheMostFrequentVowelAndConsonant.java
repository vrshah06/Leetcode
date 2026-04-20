class findTheMostFrequentVowelAndConsonantSolution
{
    public int maxFreqSum(String s)
    {
        int[] Freq = new int[26];
        int maxVowel = 0;
        int maxConsonant = 0;
        for(char ch: s.toCharArray())
        {
            Freq[ch - 'a']++;
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            {
                maxVowel = Math.max(maxVowel, Freq[ch - 'a']);
            }
            else
            {
                maxConsonant = Math.max(maxConsonant, Freq[ch - 'a']);
                
            }
        }
        return maxVowel + maxConsonant;
    }
}