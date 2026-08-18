nums = eval(input("Enter the array: "))
count = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            count+=1
print("The number of inversions in the array is:", count)