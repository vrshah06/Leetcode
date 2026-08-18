nums = eval(input("Enter the list of numbers: "))
k = int(input("Enter the maximum number of zeros allowed: "))
max_length = 0
#loop over all possible starting points of the subarray
for i in range(len(nums)):
    zero_count = 0
    #loop over all possible ending points of the subarray
    for j in range(i, len(nums)):
        #check if the current number is zero
        if nums[j] == 0:
            zero_count += 1
        if zero_count > k:
            break
        #update the max length if valid subarray is found
        max_length = max(max_length, j - i + 1)
print("The length of the longest subarray with at most", k, "zeros is:", max_length)

#Optimized solution using sliding window technique
left = 0
zero_count = 0
max_length = 0
for right in range(len(nums)):
    if nums[right] == 0:
        zero_count += 1
    if zero_count > k:
        if nums[left] == 0:
            zero_count -= 1
        left += 1
    max_length = max(max_length, right - left + 1)
print("The length of the longest subarray with at most", k, "zeros is:", max_length)   