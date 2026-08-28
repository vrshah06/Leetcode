nums = eval(input("Enter a list of numbers: "))
xor = 0
#this will work only if there is one duplicate number and all other numbers are in the range from 1 to n-1 where n is the length of the list.
# if count of number is greater than 2 then this will not work.
for num in nums:
    xor ^= num
for i in range(1, len(nums)):
    xor ^= i
print("Duplicate Number:", xor)

#Better Approach
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeated = set()

        for num in nums:
            if num in repeated:
                return num
            repeated.add(num)

        return -1