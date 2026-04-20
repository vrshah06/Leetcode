# nums = eval(input("Enter the list of numbers: "))
# n = len(nums)
# minDiff = float('inf')
# pos = {}
# for i,num in enumerate(nums):
#     rev = int(str(num)[::-1])
#     if rev in pos:
#         minDiff = min(minDiff,abs(i-pos[rev]))
#     pos[num] = i
# print(minDiff if minDiff != float('inf') else -1)
nums = eval(input("Enter the list of numbers: "))
minDiff = float('inf')

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if int(str(nums[i])[::-1]) == nums[j]:
            minDiff = min(minDiff, abs(i - j))

print(minDiff if minDiff != float('inf') else -1)