nums=eval(input("Enter a list of numbers: "))
n = len(nums)
repeating = -1
missing = -1
for i in range(1, n+1):
    count = nums.count(i)
    if count==2:
        repeating = i
    elif count==0:
        missing = i
    if repeating != -1 and missing != -1:
        break
print(f"Repeating number: {repeating}, Missing number: {missing}")

#Method 2: Using Hash Map
hash_map = [0] * (n + 1)
for num in nums:
    hash_map[num] += 1
    for i in range(1, n + 1):
        if hash_map[i] == 2:
            repeating = i
        elif hash_map[i] == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break
print(f"Repeating number: {repeating}, Missing number: {missing}")

