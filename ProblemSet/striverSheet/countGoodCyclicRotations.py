nums = eval(input("Enter the list of numbers: "))
count = 0
for i in range(len(nums)):
    nums = nums[1:] + [nums[0]]
    firstHalfSum = sum(nums[:len(nums)//2])
    secondHalfSum = sum(nums[len(nums)//2:])
    if firstHalfSum > secondHalfSum:
        count += 1
    print(f"Rotation {i + 1}: {nums}, First half sum: {firstHalfSum}, Second half sum: {secondHalfSum}")
print("The number of good cyclic rotations is:", count)