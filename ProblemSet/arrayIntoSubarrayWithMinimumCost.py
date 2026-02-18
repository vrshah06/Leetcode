nums=eval(input("Enter the list of numbers: "))
first = nums[0]
temp = nums[1:]
temp.sort()
print(first+temp[0]+temp[1])