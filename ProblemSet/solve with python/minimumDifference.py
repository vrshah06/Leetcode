l = eval(input("Enter the numbers: "))
k = input("Enter the target: ")
if k==1:
    print(0)
l.sort()
min_diff = float('inf')
for i in range(len(l)-k+1):
    curr = l[i+k-1] - l[i]
    min_diff = min(min_diff, curr)
print(min_diff)

#Part 2
l = eval(input("Enter the numbers: "))
l.sort()
temp=[]
min_diff=float('inf')
for i in range(len(l)-1):
    curr = l[i+1] - l[i]
    if curr<min_diff:
        min_diff=curr
        temp=[l[i],l[i+1]]
    elif curr==min_diff:
        temp.append([l[i],l[i+1]])
print(temp)