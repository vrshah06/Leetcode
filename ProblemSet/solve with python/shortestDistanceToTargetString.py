string = eval(input("Enter the string: "))
target = input("Enter the target string: ")
startIndex = int(input("Enter the starting index: "))
n = len(string)
minDistance = float('inf')
for i in range(n):
    if string[i]==target:
        front = (i-startIndex+n) % n
        back = (startIndex-i+n) % n
        minDistance = min(minDistance,min(front,back))
if minDistance==float('inf'):
    print(-1)
else:
    print(minDistance)