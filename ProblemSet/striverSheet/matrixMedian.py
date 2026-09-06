matrix = eval(input("Enter a matrix (list of lists): "))
elements = []
for row in matrix:
    for element in row:
        elements.append(element)
elements.sort()
median = elements[len(elements) // 2] 
print("Median of the matrix:", median)