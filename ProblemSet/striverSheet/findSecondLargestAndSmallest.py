nums = eval(input("Enter a list of numbers: "))
nums = list(set(nums))  # Remove duplicates
nums.sort()  # Sort the list
if len(nums) < 2:
    print(-1)
else:
    second_largest = nums[-2]
    second_smallest = nums[1]
    print("Second Largest:", second_largest)
    print("Second Smallest:", second_smallest)

#Method 2
nums = eval(input("Enter a list of numbers: "))
smallest = float('inf')
second_smallest = float('inf')
largest = float('-inf')
second_largest = float('-inf')
if len(nums) < 2:
    print(-1)
else:
    for num in nums:
        if num <smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)
