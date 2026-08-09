t = int(input())
for _ in range(t):
    spellCards = int(input())
    damage = list(map(int, input().split()))
    sum = 0
    isSheild=False
    for i in range(spellCards):
        if not isSheild:
            sum += damage[i]
        if i>0 and damage[i]==damage[i-1]:
            isSheild=True
    print(sum)
    