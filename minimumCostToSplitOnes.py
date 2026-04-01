n = int(input("Enter the number: "))
if n==1:
    print(0)
elif n==2:
    print(1)
elif n==3:
    print(3)
else:
    print(((n-1)**2+(n-1))//2)