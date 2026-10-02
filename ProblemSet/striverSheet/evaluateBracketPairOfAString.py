s = input("Enter the string : ")
knowledge = eval(input("Enter the knowledge : "))
d = dict(knowledge)
result = []
i = 0
while i < len(s):
    if s[i]=='(':
        j = s.find(')',i+1)
        result.append(d.get(s[i+1:j],'?'))
        i = j
    else:
        result.append(s[i])
    i += 1
print(''.join(result))