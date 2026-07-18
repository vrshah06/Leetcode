arr = eval(input("Enter the numbers:  "))
temp = sorted(set(arr))
rank = {}
for i in range(len(arr)):
    rank[arr[i]] = temp.index(arr[i]) + 1
for i in range(len(arr)):
    arr[i] = rank[arr[i]]
print(arr)
