arr = eval(input("Enter the array: "))
n = len(arr)
# Traverse through all array elements
for i in range(n-1,-1,-1):
    # Last i elements are already in place
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted array is: ",arr)