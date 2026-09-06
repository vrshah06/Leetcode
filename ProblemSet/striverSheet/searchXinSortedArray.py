nums = eval(input("Enter the array of numbers: "))
target = int(input("Enter the target number to search: "))
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        print("Target found at index:", mid)
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if low > high:
    print("Target not found in the array.")