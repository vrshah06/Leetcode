nums = eval(input("Enter the array of numbers: "))
x = int(input("Enter the number :"))
#brute force
for i in range(len(nums)):
    if nums[i]> x:
        print("The upper bound of the number is at index:",i)
        break
else:
    print("The upper bound of the number is at index:",len(nums))
#Optimized
low = 0
high = len(nums) - 1
ans = len(nums)
while low <= high:
    mid = (low + high) // 2
    if nums[mid] > x:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print("The upper bound of the number is at index:",ans)