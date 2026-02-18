n = int(input("Enter the number: "))
binary=""
temp=['0']
count=0
for i in range(n+1):
    while i>0:
        binary=str(i%2)+binary
        i//=2
    temp.append(binary)
    if binary.count('0')==len(binary) or binary.count('1')==len(binary):
        count+=1
    binary=""
print(temp)
print(count)

        