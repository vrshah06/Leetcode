nums = eval(input("Enter the array of numbers: "))
count = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        subarray = nums[i:j+1]
        if sum(subarray) % 2 != 0:
            count += 1
print("The number of subarrays with an odd sum is:", count)

# Optimized approach using prefix sums
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount, prefixSum, mod = 0, 0, 1_000_000_007
        for a in arr:
            prefixSum += a
            oddCount += prefixSum % 2
        oddCount += (len(arr) - oddCount) * oddCount
        return oddCount % mod