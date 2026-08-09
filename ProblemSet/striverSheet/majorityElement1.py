nums = eval(input("Enter the array: "))
n = len(nums)

# Hash map to store element counts
mp = {}

# Count occurrences of each element
for num in nums:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1

for num, count in mp.items():
    if count > n // 2:
        return num

# Return -1 if no majority element is found
return -1