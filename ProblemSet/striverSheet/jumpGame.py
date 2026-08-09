nums = eval(input("Enter the list of numbers: "))
max_index = 0
for i in range(len(nums)):
    if i > max_index:
        print(False)
        break
    max_index = max(max_index, i + nums[i])
print(True)