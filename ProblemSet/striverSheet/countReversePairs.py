nums = eval(input("Enter the array: "))
count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i]>(2*nums[j]):
            count+=1
print("The number of reverse pairs in the array is:", count)