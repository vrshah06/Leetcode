nums = eval(input("Enter the array of numbers: "))
mini_index = nums.index(min(nums))
maxi_index = nums.index(max(nums))
left = min(mini_index, maxi_index)
right = max(mini_index, maxi_index)
# Remove  both from the front
front = right + 1
# Remove both from the back
back = len(nums) - left
# Remove one from the front and one from the back
both  = left + 1 + (len(nums) - right)
result = min(front, back, both)
print("Minimum number of removals required:", result)

