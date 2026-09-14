s = input("Enter the string: ")
k = int(input("Enter the value of k: "))
answer = 0
for i in range(len(s)):
    # left shift the string
    s = s[1:] + s[0]
    score = 0
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            score += 1
    if score == k:
        answer += 1
print("The number of rotations with exactly", k, "equal adjacent pairs is:", answer)