nums = eval(input("Enter a sorted array: "))
n = len(nums)
ans = 0
for i in range(n):
    ans ^= nums[i]
print("The single element is:", ans)