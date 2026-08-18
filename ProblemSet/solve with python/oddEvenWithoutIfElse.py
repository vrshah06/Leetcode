nums = eval(input("Enter the numbers: "))
# without using if else statement
for num in nums:
    print(["even", "odd"][num % 2], end=" ")
