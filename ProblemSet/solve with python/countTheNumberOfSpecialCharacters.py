word = input("Enter a word: ")
count = 0
st = set(word)
for i in range(26):
    lower= chr(ord('a') + i)
    upper = chr(ord('A') + i)
    if lower in st or upper in st:
        count += 1
print("Number of special characters: ", len(st) - count)
    
    
        