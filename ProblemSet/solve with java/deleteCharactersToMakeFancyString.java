//import java.util.*;
class deleteCharactersToMakeFancyStringSolution
{
    public String makeFancyString(String s)
    {
        StringBuilder result = new StringBuilder();
        int count = 1;
        char prevChar = s.charAt(0);
        result.append(prevChar);
        for (int i =1;i<s.length();i++)
        {
            char currentChar = s.charAt(i);
            if (currentChar == prevChar) {
                count++;
                if (count < 3) {
                    result.append(currentChar);
                }
            } else {
                count = 1; // reset count for a new character
                result.append(currentChar);
            }
            prevChar = currentChar;
        }
        return result.toString();
    }

    public int fib(int n) {
        
        throw new UnsupportedOperationException("Unimplemented method 'fib'");
    }

    public long maximumTripletValue(int[] arr) {
        
        throw new UnsupportedOperationException("Unimplemented method 'maximumTripletValue'");
    }
}