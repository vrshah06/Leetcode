s = input("Enter the string: ")
score = 0
depth = 0
for char in range(len(s)):
    if s[char] == '(':
        depth += 1
    else:
        depth -= 1
        if s[char-1] == '(':
            score += 2 ** depth
print("Score of the parentheses is: ",score)

