l = eval(input("Enter the number: "))
binary = ""
num = l
temp=[]
decimal = []
for i in num:
    original=i
    while i > 0:
        binary = str(i % 2) + binary
        i //= 2
    temp.append(binary)
    r=(binary[::-1])
    binary=""
    reflect=int(r,2)
    decimal.append((reflect,original))
decimal.sort()
print ([i for _,i in decimal])