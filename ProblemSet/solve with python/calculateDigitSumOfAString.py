s = input("Enter the string: ")
k = int(input("Enter the value of k: "))
while len(s)>k:
    group = []
    for i in range(0, len(s),k):
        group.append(str(sum(int(char) for char in s[i:i+k])))
    s = ''.join(group)
print("The final string after calculating the digit sum is:", s)