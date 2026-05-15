nums = eval(input("Enter an array of numbers: "))
result = []
for num in nums:
    for digit in str(num):
        result.append(int(digit))
print(result)