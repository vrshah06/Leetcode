nums = eval(input("Enter a list of numbers: "))
n = len(nums)
if n==0:
    print("The list is empty.")
else:
    count = 0
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    print(count<=1)