nums = eval(input("Enter the array: "))
l = len(nums)
if l == 0:
    print("The array is empty.")
else:
    count = 0
    for i in range(l):
        if nums[i] > nums[(i + 1) % l]:
            count += 1
    print(count <= 1)
