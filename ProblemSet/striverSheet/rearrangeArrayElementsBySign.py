nums = eval(input("enter the list of numbers: "))
result = [0] * len(nums)
neg = []
pos = []
for i in range(len(nums)):
    if nums[i] < 0:
        neg.append(nums[i])
    else:
        pos.append(nums[i])
for i in range(len(nums)):
    if i % 2 == 0:
        result[i] = pos[i // 2]
    else:
        result[i] = neg[i // 2]
print("Rearranged array:", result)