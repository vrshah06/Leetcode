nums = eval(input("Enter the numbers: "))
next_greater = [-1] * len(nums)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            next_greater[i] = nums[j]
            break
print("Next Greater Elements to the Right:", next_greater)

#next smaller element to the right
next_smaller = [-1] * len(nums)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[i]:
            next_smaller[i] = nums[j]
            break
print("Next Smaller Elements to the Right:", next_smaller)
