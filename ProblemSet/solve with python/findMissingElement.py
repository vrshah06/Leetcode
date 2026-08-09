class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        maximum = max(nums)
        minimum = min(nums)
        result = []
        for i in range(minimum,maximum):
            if i in nums:
                continue
            else:
                result.append(i)
        return result