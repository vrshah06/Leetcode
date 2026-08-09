nums = eval(input("Enter a sorted list of numbers: "))
target = int(input("Enter the target number: "))
for num in nums:
    if num == target:
        print(nums.index(num))
        break
    else:
        nums.append(target)
        nums.sort()
        print(nums.index(target))
        break