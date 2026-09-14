nums = eval(input("Enter the list of numbers: "))
special = 0
mapping = {}
mapping[nums[0]] = 1
for i in range(1,len(nums)):
    if nums[i]!= nums[i-1]:
        mapping[nums[i]] = mapping.get(nums[i],0)+1
for value in mapping.values():
    if value == 1:
        special += 1
print("The number of integers appearing in a single block is:", special)