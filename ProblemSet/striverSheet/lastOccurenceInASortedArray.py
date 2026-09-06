nums = eval(input("Enter the array of numbers: "))
target = int(input("Enter the number :"))
last_occurrence = -1
for i in range(len(nums)):
    if nums[i] == target:
        last_occurrence = i
print("The last occurrence of the number is at index:", last_occurrence)