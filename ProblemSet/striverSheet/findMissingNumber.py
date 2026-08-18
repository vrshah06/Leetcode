nums = eval(input("Enter the array: "))
n = len(nums)
nums.sort()
max_num = nums[-1]
min_num = nums[0]
for i in range(min_num, max_num + 1):
    if i not in nums:
        print("Missing number is:", i)
        break
