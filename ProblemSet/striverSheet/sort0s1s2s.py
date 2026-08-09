class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroCount = 0
        oneCount = 0
        twoCount = 0
        for num in nums:
            if num==0:
                zeroCount+=1
            elif num==1:
                oneCount+=1
            else:
                twoCount+=1
        i=0
        while zeroCount > 0:
            nums[i] = 0
            zeroCount -= 1
            i += 1

        while oneCount > 0:
            nums[i] = 1
            oneCount -= 1
            i += 1

        while twoCount > 0:
            nums[i] = 2
            twoCount -= 1
            i += 1
        return nums
            

        
        