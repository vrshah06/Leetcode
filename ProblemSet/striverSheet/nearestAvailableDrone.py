nums = eval(input("Enter the list of drone positions: "))
target  = eval(input("Enter the target position: "))
best_distance = float('inf')
best = -1
for i,(x,y,r) in enumerate(nums):
    dist = abs(x - target[0]) + abs(y - target[1])
    if dist <= r and dist < best_distance:
        best_distance = dist
        best = i
print(best)
