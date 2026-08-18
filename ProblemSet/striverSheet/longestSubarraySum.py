nums = eval(input("Enter a list of numbers: "))
k = int(input("Enter the target sum: "))
n = len(nums)
maxLength = 0
for i in range(n):
    for j in range(i, n):
        current = 0
        for l in range(i,j+1):
            current += nums[l]
        if current == k:
            maxLength = max(maxLength, j-i+1)
print("Length of the longest subarray with sum", k, "is:", maxLength)