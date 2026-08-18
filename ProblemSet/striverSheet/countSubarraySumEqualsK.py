nums = eval(input("enter the list of numbers: "))
k = int(input("enter the target sum: "))
n = len(nums)
count = 0
for i in range(n):
    for j in range(i,n):
        sum =0
        for l in range(i,j+1):
            sum += nums[l]
        if sum == k:
            count += 1
print(count)

#better approach
count = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += nums[j]
        if sum == k:
            count += 1
print(count)
        