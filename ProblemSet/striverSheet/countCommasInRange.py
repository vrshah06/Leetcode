n = int(input("enter the number : "))
count = 0
if n<1000:
    print("0")
else:
    for i in range(1000, n + 1):
            count += 1
    print(count)
