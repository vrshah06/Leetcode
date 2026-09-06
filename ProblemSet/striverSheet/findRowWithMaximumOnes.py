nums = eval(input("Enter a list of lists: "))
maxCount = 0
index = -1
rows = len(nums)
cols = len(nums[0])
for row in range(rows):
    ones = 0
    for col in range(cols):
        ones += nums[row][col]
    if ones > maxCount:
        maxCount = ones
        index = row
print("Row with maximum number of 1s:", index) 