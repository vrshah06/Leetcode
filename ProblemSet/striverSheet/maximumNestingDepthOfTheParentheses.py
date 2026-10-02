s = input("Enter the string: ")
depth = 0
r = 0
for ch in s:
    if ch == ')':
        depth -= 1
        continue
    if ch != '(':
        continue
    depth += 1
    r = max(r, depth)
print(r)