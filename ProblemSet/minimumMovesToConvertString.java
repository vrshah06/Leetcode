//import java.util.*;
class minimumMovesSolution
{
    public int minimumMoves(String s)
    {
        //Scanner sc = new Scanner(System.in);
        int n = s.length();
        int count = 0;
        for(int i = 0;i<n;i++)
        {
            if(s.charAt(i)=='X')
            {
                count++;
                i+=2;
            }
        }
        return count;
    }
}
