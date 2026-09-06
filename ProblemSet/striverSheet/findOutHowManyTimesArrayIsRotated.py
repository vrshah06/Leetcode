nums = eval(input("Enter the array of numbers: "))
n = len(nums)
minValue = nums[0]
minIndex = 0
for i in range(1, n):
    if nums[i] < minValue:
        minValue = nums[i]
        minIndex = i
print("The array is rotated", minIndex, "times.")