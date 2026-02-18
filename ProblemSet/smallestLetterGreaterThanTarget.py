letters=eval(input("Enter the list of letters: "))
target=input("Enter the target letter: ")
for letter in letters:
    if letter>target:
        print(letter)
        break
else:
    print(letters[0])