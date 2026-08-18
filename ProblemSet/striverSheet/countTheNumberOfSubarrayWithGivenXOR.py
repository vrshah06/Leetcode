nums = eval(input("Enter the array: "))
k = int(input("Enter the target XOR value: "))
count = 0
#Brute Force Approach
for i in range(len(nums)):
    xor_value = 0
    for j in range(i, len(nums)):
        xor_value ^= nums[j]
        if xor_value == k:
            count += 1
print("The number of subarrays with XOR equal to", k, "is:", count)
