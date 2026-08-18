nums = eval(input("Enter a  array: "))
n = len(nums)
for i in range(n):
    left = (i==0) or (nums[i]>nums[i-1])
    right = (i==n-1) or (nums[i]>nums[i+1])
    if left and right:
        print("Peak element index is:", i)
