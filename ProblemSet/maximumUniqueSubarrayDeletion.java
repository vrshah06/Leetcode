import java.util.*;

class maximumUniqueSubarrayDeletionSolution
{
    public int maxSum(int[] nums) 
    {
        Set<Integer> set = new HashSet<>();
        for(int num: nums)
        {
            set.add(num);
        }
        int Sum = 0;
        for(int num: set)
        {
            if(num>=0)
            {
                Sum += num;
            }
        }
        if (Sum==0) {
            Sum= Collections.max(set);
            
        }
        return Sum;
    }
}