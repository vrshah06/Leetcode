patterns = eval(input("Enter the list of patterns: "))
word = input("Enter the word: ")
count = 0
for pattern in patterns:
    if pattern in word:
        count += 1
print("The number of patterns that appear as substrings in the word is:", count)