s = input("Enter the string: ")
leftMin = 0
leftMax = 0
for char in s:
    if char == '(':
        leftMin += 1
        leftMax += 1
    elif char == ')':
        leftMin -= 1
        leftMax -= 1
    else:
        leftMin -= 1
        leftMax += 1
    if leftMax < 0:
        print("False")
        break
    if leftMin < 0:
        leftMin = 0
    print("True" if leftMin == 0 else "False")