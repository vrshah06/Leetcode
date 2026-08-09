nums = eval(input("Enter a list of numbers: "))
n = len(nums)
maxSum = float('-inf')
currentSum = 0
for num in nums:
    currentSum += num
    maxSum = max(maxSum, currentSum)
    if currentSum < 0:
        currentSum = 0
print(maxSum)