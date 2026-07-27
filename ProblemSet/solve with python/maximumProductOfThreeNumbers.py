nums = eval(input("Enter a list of integers: "))
l1 = float('-inf')
l2 = float('-inf')
l3 = float('-inf')

s1 = float('inf')
s2 = float('inf')
for num in nums:
    if num > l1:
        l3 = l2
        l2 = l1
        l1 = num
    elif num > l2:
        l3 = l2
        l2 = num
    elif num > l3:
        l3 = num

    if num < s1:
        s2 = s1
        s1 = num
    elif num < s2:
        s2 = num
product1 = l1 * l2 * l3
product2 = l1 * s1 * s2
max_product = max(product1, product2)
print("The maximum product of three numbers in the list is:", max_product)
