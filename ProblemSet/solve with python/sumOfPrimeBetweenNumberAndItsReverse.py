n = int(input("Enter a number: "))
temp = n
rev=0
sum=0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if n > rev:
    n, rev = rev, n
for num in range(n,rev+1):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            sum += num
print(sum)