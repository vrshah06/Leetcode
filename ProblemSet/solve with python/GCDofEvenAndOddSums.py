n = int(input("Enter the number: "))
gcd = 1
evenSum = (n * n)+n
oddSum = (n * n)
print("The sum of even numbers is:", evenSum)
print("The sum of odd numbers is:", oddSum)

if evenSum == 0 or oddSum == 0:
    gcd = max(evenSum, oddSum)
else:
    for i in range(1, min(evenSum, oddSum) + 1):
        if evenSum % i == 0 and oddSum % i == 0:
            gcd = i

print("The GCD of the sums of even and odd numbers is:", gcd)