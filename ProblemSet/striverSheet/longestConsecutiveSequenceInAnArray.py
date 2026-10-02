nums = eval(input("Enter a list of numbers: "))
nums = list(set(nums))
max_num = max(nums)
min_num = min(nums)
print(nums)
for i in range(min_num, max_num + 1):
    if i not in nums:
        print(f"The longest consecutive sequence is: {i - 1}")
        break
else:
    print(f"The longest consecutive sequence is: {len(nums)}")