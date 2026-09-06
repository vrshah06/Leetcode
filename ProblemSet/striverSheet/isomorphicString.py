s = input("Enter the first string: ")
t = input("Enter the second string: ")

if len(s) != len(t):
    print("The strings are not isomorphic.")
else:
    mapping={}
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                print("The strings are not isomorphic.")
                break
        else:
            if t[i] in mapping.values():
                print("The strings are not isomorphic.")
                break
            mapping[s[i]] = t[i]
    else:
        print("The strings are isomorphic.")
