n = int(input("Enter the number: "))
binary = ""
if n==0:
    binary="0"
else:
    while n>0:
        binary = str(n%2)+binary
        n//=2
print(binary)
complement = ""
for digit in binary:
    if digit=="0":
        complement += "1"
    else:
        complement += "0"
print("Complement:", complement)
temp=int(complement,2)
print("Complement in decimal:", temp)