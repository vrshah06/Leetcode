nums = eval(input("Enter the array: "))
target = int(input("Enter the element to search for: "))
for i in range(len(nums)):
    if nums[i] == target:
        print("Element found at index:", i)
        break
else:
    print("Element not found in the array")