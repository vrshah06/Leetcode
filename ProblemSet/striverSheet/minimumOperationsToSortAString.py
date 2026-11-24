s = input("Enter the string: ")
n = len(s)
if all(s[i] <= s[i + 1] for i in range(n - 1)):
    print(0)
if n== 2:
    print(-1)
mn = min(s)
mx = max(s)
if s[0]== mn or s[-1]==mx:
    print(1)
if any(c == mn or c == mx for c in s[1:-1]):
    print(2)
print(3)