nums = eval(input("Enter a list of integers: "))
temp = []
for i in range(len(nums)):
    count = 0
    for j in range(i + 1, len(nums)):
        if (i<j and nums[i]%2==0 and nums[j]%2!=0) or (i<j and nums[i]%2!=0 and nums[j]%2==0):
            count += 1
    temp.append(count)
print(temp)