digits = input("Enter the digits: ")
result = []
mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}
#all combinations of letters for the given digits
#for digits=34 output is ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']
for digit in digits:
    if digit in mapping:
        letters = mapping[digit]
        if not result:
            result = list(letters)
        else:
            prev_result = result
            result = []
            for letter in letters:
                for prev in prev_result:
                    result.append(prev + letter)
print("All combinations of letters for the given digits", digits, "are:")
print(result)
                    