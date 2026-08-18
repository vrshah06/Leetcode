s = input("Enter the string: ")
i = 0
result = 0
count = {}
for j,ch in enumerate(s):
    count[ch] = count.get(ch, 0) + 1
    while count[ch] > 2:
        count[s[i]] -= 1
        i+=1
    result = max(result, j-i+1)
print("The length of the longest substring with at most two occurrences is:", result)

        

