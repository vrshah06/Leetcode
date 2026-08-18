s = input("Enter the string: ")
index = -1
for i in range(len(s)-1, -1, -1):
    if int(s[i]) % 2 != 0:
        index = i
        break
i = 0 
while i <= index and s[i] == '0':
    i += 1
ans = s[i:index+1]
print(str(ans))
