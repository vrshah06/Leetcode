nums = eval(input("Enter the numbers: "))
k = int(input("Enter the number of rotations: "))
n = len(nums)
k = k%n
nums.reverse()
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])
print(nums)