nums = eval(input("Enter the list of numbers: "))
max_xor=0
for i in range(len(nums)):
    for j in range(0,len(nums)):
        max_xor=max(max_xor,nums[i]^nums[j])
print(max_xor)