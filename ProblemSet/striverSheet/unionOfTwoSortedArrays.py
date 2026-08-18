arr1 = eval(input("Enter the first sorted array: "))
arr2 = eval(input("Enter the second sorted array: "))
arr1.sort()
arr2.sort()
freq={}
for i in arr1:
    freq[i]=freq.get(i,0)+1
for i in arr2:
    freq[i]=freq.get(i,0)+1
print("Union of the two sorted arrays:", list(freq.keys()))