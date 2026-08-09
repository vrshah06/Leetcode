sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
print(" ".join(words))

#Method 2
sentence = input("Enter a sentence: ")
words = []
word = ""
for ch in sentence:
    if ch != " ":
        word+=ch
    elif word:
        words.append(word)
        word = ""
if word:
    words.append(word)
words.reverse()
print(" ".join(words))