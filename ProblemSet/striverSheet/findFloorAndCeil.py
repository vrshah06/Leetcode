nums = eval(input("Enter the array of numbers: "))
x = int(input("Enter the number :"))
low = 0
high = len(nums) - 1
floor = -1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] <= x:
        floor = nums[mid]
        low = mid + 1
    else:
        high = mid - 1
    print("Current mid:", mid, "Current floor:", floor)

low = 0
high = len(nums) - 1
ceil = -1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= x:
        ceil = nums[mid]
        high = mid - 1
    else:
        low = mid + 1
    print("Current mid:", mid, "Current ceil:", ceil)
