class Solution:
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()
# Main code
m = int(input("Enter the size of first array: "))
n = int(input("Enter the size of second array: "))

nums1 = [0] * (m + n)
nums2 = [0] * n

print("Enter the elements of first array:")
for i in range(m):
    nums1[i] = int(input())

print("Enter the elements of second array:")
for i in range(n):
    nums2[i] = int(input())

print("The merged array is:")

s = Solution()
s.merge(nums1, m, nums2, n)

print(*nums1)
