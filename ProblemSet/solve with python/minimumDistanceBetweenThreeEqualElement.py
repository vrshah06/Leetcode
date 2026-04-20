nums = eval(input("Enter the numbers: "))
if len(nums) <= 2:
    print(-1)
ans = float('inf')
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            for k in range(j+1,len(nums)):
                if nums[j] == nums[k]:
                    ans = min(ans, 2*(k-i))
if ans == float('inf'):
    print(-1)
else:
    print(ans)