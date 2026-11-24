nums = eval(input("Enter the numbers: "))

minMerged = float('inf')
mergedNum = ""

for i in range(0, len(nums), 2):
    mergedNum = str(nums[i]) + str(nums[i+1])

    if int(mergedNum) < minMerged:
        minMerged = int(mergedNum)

print(f"The minimum value of the merged integer is: {minMerged}")