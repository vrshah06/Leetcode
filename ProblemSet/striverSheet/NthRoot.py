M = int(input("Enter a number: "))
N = int(input("Enter the root: "))
ans = 0
for i in range(1, M + 1):
    power = i ** N
    if power == M:
        ans = i
        break
    if power > M:
        break
if ans == 0:
    print(-1)
print(ans)