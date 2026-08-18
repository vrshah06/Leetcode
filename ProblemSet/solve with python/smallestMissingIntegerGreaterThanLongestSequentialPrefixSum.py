nums = eval(input("Enter the array: "))
prefix_sum = nums[0]
for i in range(1, len(nums)):
    if nums[i]==nums[i-1]+1:
        prefix_sum += nums[i]
    else:
        break
seen = set(nums)
answer = prefix_sum
print(answer)
while answer in seen:
    answer += 1
print("The smallest missing integer greater than the longest sequential prefix sum is:", answer)