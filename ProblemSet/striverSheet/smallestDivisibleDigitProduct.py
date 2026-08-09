n = int(input("Enter a number: "))
t = int(input("Enter the number to divide by: "))
while True:
    product = 1
    for i in str(n):
        product *= int(i)
    if product % t == 0:
        print(n)
        break
    n += 1

#Method 2
n = int(input("Enter a number: "))
t = int(input("Enter the number to divide by: "))
while True:
    product = 1
    if '0' in str(n):
        n += 1
        continue
    for i in str(n):
        product *= int(i)
    if product % t == 0:
        print(n)
        break
    temp = int(n)
    n += 1

    if product == 1:
        print(-1)
        break
