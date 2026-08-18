nums = eval(input("Enter a list of numbers: "))
n = len(nums)
ans = []
subsets = 1<<n
for i in range(subsets):
    temp = []
    for j in range(n):
        if (i & (1<<j)):
            temp.append(nums[j])
    ans.append(temp)
print(ans)