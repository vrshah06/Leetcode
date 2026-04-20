nums1 = eval(input("Enter the first sorted array: "))
nums2 = eval(input("Enter the second sorted array: "))
merged = (sorted(nums1 + nums2))
n = len(merged)
if n % 2 == 0:
    median = (merged[n // 2 - 1] + merged[n // 2]) / 2
else:
    median = merged[n // 2]
print("The median of the two sorted arrays is:", float(median))
