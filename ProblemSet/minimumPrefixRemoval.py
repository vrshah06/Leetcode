nums= eval(input("Enter the list of numbers: "))
for i in range(len(nums)-1,-1,-1):
    if nums[i-1]>=nums[i]:
        print(i)
    else:
        print(0)
