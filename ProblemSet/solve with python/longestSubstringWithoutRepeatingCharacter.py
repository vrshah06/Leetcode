s = input("Enter the string: ")
i = 0
result = 0
count = {}
#aaabbbccc
#j=0 ch=a
#j=1 ch=a, j=2 ch=a, j=3 ch=b, j=4 ch=b, j=5 ch=b, j=6 ch=c, j=7 ch=c, j=8 ch=c
for j,ch in enumerate(s):
    count[ch] = count.get(ch, 0) + 1
    while count[ch] > 1:
        count[s[i]] -= 1
        i+=1
    result = max(result, j-i+1)
print("The length of the longest substring without repeating characters is:", result)