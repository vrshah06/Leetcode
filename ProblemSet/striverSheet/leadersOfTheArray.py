nums = eval(input("Enter the array: "))
n = len(nums)
result = []
for i in range(n):
    isLeader = True
    for j in range(i+1,n):
        if nums[j]>=nums[i]:
            isLeader = False
            break
    if isLeader:
        result.append(nums[i])
print("Leaders of the array are: ",result)
