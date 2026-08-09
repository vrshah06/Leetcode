nums = eval(input("Enter a list of numbers: "))
n = len(nums)
maxProduct = nums[0]
# Outer loop picks the starting index
for i in range(len(nums)):
    # Initialize current product to 1
    prod = 1

    # Inner loop picks the ending index
    for j in range(i, len(nums)):
        # Multiply current number to product
        prod *= nums[j]

        # Update maximum product if needed
        maxProduct = max(maxProduct, prod)

# Return the result
print(maxProduct)