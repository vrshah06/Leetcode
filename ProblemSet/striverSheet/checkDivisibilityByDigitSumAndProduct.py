n = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(n))
digit_product = 1
for digit in str(n):
    digit_product *= int(digit)
total = digit_sum + digit_product
if n % total == 0:
    print(True)
else:
    print(False)