import math
nums = eval(input("Enter a list of numbers: "))
threshold = int(input("Enter the threshold: "))
n = len(nums)
max_num = max(nums)
for d in range(1,max_num+1):
    total = 0
    for num in nums:
        total += math.ceil(num/d)
    if total <= threshold:
        print(d)
        break
print(-1)