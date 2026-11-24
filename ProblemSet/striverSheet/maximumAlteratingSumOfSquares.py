nums = eval(input("Enter a list of numbers: "))
n = len(nums)
#square every number and sort the list in a ascending order
squared = sorted([x**2 for x in nums])
oddIndex = n//2
totalSum = sum(squared[oddIndex:]) - sum(squared[:oddIndex])
print("The maximum alternating sum of squares is:", totalSum)

