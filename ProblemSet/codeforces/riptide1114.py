t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    rounds = 0
    while True:
        if a == b or b == c or a == c:
            print(rounds)
            break
        else:
            arr = [a, b, c]
            maxIndex = arr.index(max(arr))
            minIndex = arr.index(min(arr))
            arr[maxIndex] -= 1
            arr[minIndex] += 1
            a, b, c = arr
            rounds += 1
    
    