nums = eval(input("Enter the array of numbers: "))
sum = 0
arr= []
for i in range(len(nums)):
    for j in range(i+1):
        arr.append(nums[j])
        set_arr = set(arr)
        sum += len(set_arr) ** 2
    arr = []  # Reset the array for the next iteration
print(f"The sum of squares of distinct elements in all subarrays is: {sum}")

#Secondary approach
ans = 0
n = len(nums)
for i in range(n):
    seen = set()
    for j in range(i, n):
        seen.add(nums[j])
        ans += len(seen) ** 2