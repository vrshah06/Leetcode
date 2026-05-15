nums = eval(input("Enter the array: "))
nums.sort()
l = len(nums)
if l==0:
    print("The array is empty.")
else:
    print("The minimum element in the rotated sorted array is:", nums[0])