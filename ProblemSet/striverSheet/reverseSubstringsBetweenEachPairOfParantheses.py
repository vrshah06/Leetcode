s = input("Enter the string : ")
answer = []
start = []
for ch in s:
    if ch == '(':
        start.append(len(answer))
    elif ch == ')':
        left  = start.pop()
        right = len(answer)-1
        while left < right:
            answer[left], answer[right] = answer[right], answer[left]
            left += 1
            right -= 1
    else:
        answer.append(ch)
print(''.join(answer))