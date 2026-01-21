public class successfulPairsOfSpellsAndPotions 
{
    public static void main(String[] args) 
    {   
        int[] spell={5,1,3};
        int[] potion={1,2,3,4,5};
        int success=7;
        int[] result=new int[spell.length];
        for(int i=0;i<spell.length;i++)
        {
            int count=0;
            for(int j=0;j<potion.length;j++)
            {
                if(spell[i]*potion[j]>=success)
                {
                    count++;
                }
            }
            result[i]=count;
        }
        
    }
}
