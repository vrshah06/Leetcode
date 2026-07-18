nums = eval(input("Enter the numbers: "))
nums.sort()
smallest = nums[0]
largest = nums[-1]
gcd=1
for i in range(1, smallest+1):
    if smallest % i == 0 and largest % i == 0:
        gcd = i
print("The GCD of the given numbers is:", gcd)