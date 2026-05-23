nums= eval(input("Enter the array: "))
target = int(input("Enter the target: "))
l = len(nums)
if l==0:
    print("The array is empty.")
else:
    for i, num in enumerate(nums):
        if num == target:
            print("The target is found at index:", i)
            break
    else:
        print(-1)