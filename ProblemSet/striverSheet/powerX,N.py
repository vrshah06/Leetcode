x = int(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
if n==0 or x==1:
    print(1)
temp = n
if n<0:
    x = 1/x
    temp = -1*n
ans =1 
for i in range(1,temp+1):
    ans = ans*x
print(ans)

#Method 2
def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        ans = power(x, n // 2)
        return ans * ans
    else:
        ans = power(x, n // 2)
        return ans * ans * x

x = int(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
print(power(x, n))