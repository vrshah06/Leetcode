l = eval(input("Enter the numbers: "))
leftsum=0
rightsum = 0
evenCount = 0
for i in range(len(l)):
    left = l[:i+1:]
    for j in left:
        leftsum += j
    right = l[i+1::]
    for k in right:
        rightsum+=k
    if (leftsum-rightsum)%2==0:
        evenCount+=1
    if evenCount==0:
        print(0)
print(evenCount-1)
        