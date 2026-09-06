nums = eval(input("Enter a list of numbers: "))
k = int(input("Enter the value of k: "))
minIndex = float('inf')
for i in range(len(nums)):
    instability = 0
    firstHalf = nums[:i+1]
    secondHalf = nums[i:]
    print (f"First half: {firstHalf}, Second half: {secondHalf}")
    maxFirstHalf = max(firstHalf)
    minSecondHalf = min(secondHalf)
    instability = maxFirstHalf - minSecondHalf
    if instability <= k:
        minIndex = min(minIndex, i)
        print(i)
if minIndex == float('inf'):
    print("No valid index found.")
print("Final answer:", minIndex)