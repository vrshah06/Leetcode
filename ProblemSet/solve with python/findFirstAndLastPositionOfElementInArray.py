nums = eval(input("Enter a list of numbers: "))
target = eval(input("Enter the target number: "))
nums.sort()
first = -1
last = -1
for i in range(len(nums)):
    if nums[i]== target:
        first = i
        break
for i in range(len(nums)-1, -1, -1):
    if nums[i]== target:
        last = i
        break
result = [first, last]
print("Resultant Array:", result)

#Binary Search Approach
low = 0
high = len(nums) - 1
first = -1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        first = mid
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
low = 0
high = len(nums) - 1
last = -1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        last = mid
        low = mid + 1
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
result = [first, last]
print("Resultant Array:", result)
