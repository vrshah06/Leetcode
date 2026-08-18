nums = eval(input("Enter a list of numbers: "))
unique_num = 0
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if count == 1:
        unique_num = nums[i]
        break

print("The number that appears only once is:", unique_num)

#Optimized solution using XOR operation
unique_num = 0
for num in nums:
    unique_num ^= num

print("The number that appears only once is:", unique_num)