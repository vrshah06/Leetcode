s = input("Enter the string: ")
k = int(input("Enter the value of k: "))
ans = ""
n = len(s)
for i in range(n):
    oneCount = 0
    current = ""
    for j in range(i, n):
        current += s[j]
        if s[j] == '1':
            oneCount += 1
        if oneCount > k:
            break
        if ans == "" or len(current) < len(ans) or (len(current) == len(ans) and current < ans):
            ans = current
print(ans)