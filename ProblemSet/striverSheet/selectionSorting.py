arr = eval(input("Enter the array: "))
n = len(arr)
#Traverse through all array elements
for i in range(n-1):
    min_index = i
    #Find the minimum element in remaining unsorted array
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index = j
    #Swap the found minimum element with the first element
    arr[i]=arr[min_index]
    arr[min_index]=arr[i]
print("Sorted array is: ",arr)