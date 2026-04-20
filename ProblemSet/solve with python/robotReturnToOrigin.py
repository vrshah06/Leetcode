moves = input("Enter the String of moves : ")
x,y=0,0
temp1,temp2=x,y
print(x,y)
for move in moves:
    if move=='U':
        temp2+=1
        print(temp1,temp2)
    if move=='D':
        temp2-=1
        print(temp1,temp2)
    if move=='R':
        temp1+=1
        print(temp1,temp2)
    if move=='L':
        temp1-=1
        print(temp1,temp2)
if temp1==x and temp2==y:
    print(True)
else:
    print(False)