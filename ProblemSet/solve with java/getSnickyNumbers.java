class Solution 
{
    public int[] getSneakyNumbers(int[] nums)
    {
        int n = nums.length;
        int count =0 ;
        int[] sneakyNumbers = new int[2];
        for (int i =0;i<n;i++)
        {
            for(int j = i+1;j<n;j++)
            {
                if(nums[i]==nums[j])
                {
                    sneakyNumbers[count++] = nums[i];
                }
            }

        }
        return sneakyNumbers;
    }
}