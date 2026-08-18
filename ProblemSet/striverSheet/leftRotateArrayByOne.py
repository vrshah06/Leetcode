nums = eval(input("Enter the array: "))
k = int(input("Enter the number of positions to rotate: "))
temp = nums.copy()  # Create a copy of the original array to display after rotation
for i in range(len(nums)):
    nums[i]=temp[(i + k) % len(nums)]
#rotate the array by k positions to the right
for i in range(len(nums)):
    nums[i]=temp[(i - k) % len(nums)]
print("Array after left rotation by", k, "positions:", nums)