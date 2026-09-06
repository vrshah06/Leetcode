matrix = eval(input("Enter the matrix: "))
target = int(input("Enter the target value: "))
rows = len(matrix)
cols = len(matrix[0])
i = rows - 1
j = 0
while i >= 0 and j < cols:
    if matrix[i][j] == target:
        print(f"The target value {target} is found at position ({i}, {j})")
        break
    elif matrix[i][j] < target:
        j += 1
    else:
        i -= 1
print(f"The target value {target} is not found in the matrix.")