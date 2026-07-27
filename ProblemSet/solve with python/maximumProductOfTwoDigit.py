num = input("Enter a  number: ")
nums = []
for digit in num:
    nums.append(int(digit))
nums.sort()
max_product = (nums[-1]) * (nums[-2])
print("The maximum product of two digits in the number is:", max_product)
