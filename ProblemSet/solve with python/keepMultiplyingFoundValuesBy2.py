l = list(eval(input("Enter the list: ")))
original = int(input("Enter the number: "))
flag=True
while flag==True:
    if original in l:
        original*=2
    else:
        flag=False
print(original)
    