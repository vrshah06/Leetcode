coor = eval(input("Enter the coordinates : "))
degree = [0] * len(coor)
for i in range(len(coor)):
    for j in range(len(coor)):
        if coor[i][j]==1:
            degree[i] += 1

print("The degree of each vertex is:", degree)