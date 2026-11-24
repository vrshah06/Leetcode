s = input("Enter the string: ")
for i in range(len(s)-1):
    if s[i] == 'b' and s[i+1] == 'a':
        print("False")
        break
else:
    print("True")