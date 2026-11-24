arr1 = eval(input("Enter the first array: "))
arr2 = eval(input("Enter the second array: "))
d = int(input("Enter the distance value: "))
count = 0 
for i in arr1:
    if self.isValid(i, arr2, d):
        count += 1
        print(f"Element {i} is valid.")
print(f"The number of valid elements is: {count}")
def isValid(num, arr2, d):
    for j in arr2:
        if abs(num - j) <= d:
            return False
    return True

# class Solution:
#     def findTheDistanceValue(self, arr1, arr2, d):
#         c = 0
#         for n in arr1:
#             if self.isValid(n, arr2, d):
#                 c += 1
#         return c

#     def isValid(self, n, arr, d):
#         for e in arr:
#             if abs(e - n) <= d:
#                 return False
#         return True