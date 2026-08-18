n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
# gcd = 1
# n1Factors = []
# n2Factors = []
# for i in range(1,n1+1):
#     if n1 % i == 0:
#         n1Factors.append(i)
# for i in range(1,n2+1):
#     if n2 % i == 0:
#         n2Factors.append(i)
# for factor in n1Factors:
#     if factor in n2Factors:
#         gcd *= factor
# print("The GCD of", n1, "and", n2, "is", gcd)

#Optimal
a=n1
b=n2
while a>0 and b>0:
    if a>b:
        a = a % b
    else:
        b = b % a
if a == 0:
    print("The GCD of", n1, "and", n2, "is", n2)
else:
    print("The GCD of", n1, "and", n2, "is", n1)