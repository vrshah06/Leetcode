s = input("Enter the string: ")
balance = 0
result= []
for char in s: 
    if char == '(':
        if balance > 0:
            result.append(char)
        balance += 1
    else:
        balance -= 1
        if balance >0:
            result.append(char)
print("".join(result))