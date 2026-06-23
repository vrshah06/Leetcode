nums = eval(input("Enter the list of numbers: "))
sum = []
for num in nums:
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    sum.append(digit_sum)
print("Minimum element after replacement digit sum: ", min(sum))