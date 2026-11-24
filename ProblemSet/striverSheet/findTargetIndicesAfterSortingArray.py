nums = eval(input("Enter the array of numbers: "))
target = int(input("Enter the target number: "))
# Sort the array
nums.sort()
indices = []
for i in range(len(nums)):
    if nums[i] == target:
        indices.append(i)
print(f"The indices of the target number {target} after sorting the array are: {indices}")