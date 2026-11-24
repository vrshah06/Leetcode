s = input("Enter the string: ")
open = 0
add = 0
for char in s:
    if char == '(':
        open += 1
    elif char == ')':
        if open > 0:
            open -= 1
        else:
            add += 1
print("Minimum number of parentheses to add to make the string valid is: ", add + open)