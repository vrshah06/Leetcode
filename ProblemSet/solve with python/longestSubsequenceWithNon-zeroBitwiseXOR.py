nums = eval(input("Enter a list of numbers: "))
max_length = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        xor_result = 0
        for k in range(i, j + 1):
            xor_result ^= nums[k]
        if xor_result != 0:
            max_length = max(max_length, j - i + 1)
print(max_length)

#Method 2
xor = 0
has_zero = False
for num in nums:
    xor ^= num
    if num != 0:
        has_zero = True
if xor != 0:
    print(len(nums))
if has_zero:
    print(len(nums) - 1)
print(0)