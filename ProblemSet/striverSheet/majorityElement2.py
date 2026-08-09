nums= eval(input("Enter a list of numbers: "))
n = len(nums)
mp = {}
mini = n//3 +1
majority_elements = []
for num in nums:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1
    if mp[num] == mini:
        majority_elements.append(num)
    if len(majority_elements) ==2:
        break
print(majority_elements)