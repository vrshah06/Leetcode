strr = input("Enter the string : ")
total = 0
for i,c in enumerate(strr):
    reverse = 26 - (ord(c) - ord('a'))
    position = i + 1
    total += reverse * position
print("The degree of the string is : ", total)