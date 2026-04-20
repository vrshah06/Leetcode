nums = eval(input("Enter the numbers: "))
target = int(input("Enter the target: "))
start = int(input("Enter the start: "))
min_distance = float('inf')
for i in range(len(nums)):
    if nums[i] == target:
        distance = abs(i - start)
        min_distance = min(min_distance, distance)
print(min_distance)