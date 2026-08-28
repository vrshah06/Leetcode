nums = eval(input("Enter the list of numbers: "))
arr1 = []
arr2 = []
arr1.append(nums[0])
arr2.append(nums[1])
for i in range(2, len(nums)):
    if arr1[-1]> arr2[-1]:
        arr1.append(nums[i])
    else:
        arr2.append(nums[i])
print("Array 1:", arr1)
print("Array 2:", arr2)
result = arr1 + arr2
print("Resultant Array:", result)