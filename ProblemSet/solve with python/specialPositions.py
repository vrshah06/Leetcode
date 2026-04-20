mat = eval(input("Enter a 2D matrix: "))
m = len(mat)
n = len(mat[0])
count = 0
rowc = [0] * m
colc = [0] * n
for i in range(m):
    for j in range(n):
        if mat[i][j] == 1:
            rowc[i] += 1
            colc[j] += 1
for i in range(m):
    for j in range(n):
        if mat[i][j] == 1 and rowc[i] == 1 and colc[j] == 1:
            count += 1
print(count)