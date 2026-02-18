num = int(input("Enter the number: "))

binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
b=True
for i in range(len(binary)-1):
    if binary[i]==binary[i+1]:
        b = False
        break
print(b)
print("Binary:", binary)