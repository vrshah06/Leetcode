//import java.util.*;
class findTheKthCharacterInAStringSolution
{
    public char kthCharacter(int k)
    {
        if (k < 1) {
            throw new IllegalArgumentException("k must be a positive integer");
        }
        StringBuilder sb = new StringBuilder("a");
        //int size = sb.length();
        while (sb.length()<k) {
            int size = sb.length();
            for(int i =0 ;i<size;i++)
            {
                sb.append((char)(('a'+ ((sb.charAt(i)-'a')+1)%26)));
            }
        }
        return sb.charAt(k - 1);
    }
}