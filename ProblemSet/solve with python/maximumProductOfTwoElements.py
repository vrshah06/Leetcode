nums = eval(input("Enter a list of integers: "))
nums.sort()
max_product = (nums[-1]-1) * (nums[-2]-1)
print("The maximum product of two elements in the list is:", max_product)