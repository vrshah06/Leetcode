nums = eval(input("Enter a list of numbers: "))
n = len(nums)
x = int(input("Enter the number to count occurrences of: "))
count = 0
for i in nums:
    if i == x:
        count += 1
print(count)