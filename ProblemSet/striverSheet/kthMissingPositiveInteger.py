nums = eval(input("Enter the list of numbers: "))
k = int(input("Enter the value of k: "))
while k > 0:
    for i in range(1, 1000):
        if i not in nums:
            k -= 1
            if k == 0:
                print(f"The missing positive integer is: {i}")
                break

#optimized solution
low = 0
high = len(nums) - 1
while low <= high:
    mid = (low+high) // 2
    missing = nums[mid] - (mid + 1)
    if missing < k:
        low = mid + 1
    else:
        high = mid - 1
print(k+high+1)

