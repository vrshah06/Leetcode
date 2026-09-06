nums = eval(input("Enter the list of numbers: "))
total_sum = 0
# to find the starting index
for i in range(len(nums)):
    # to find the ending index
    mini = nums[i]
    for j in range(i, len(nums)):
        mini = min(mini, nums[j])
        total_sum += mini
print("The sum of the minimums of all subarrays is:", total_sum % 1000000007)
        