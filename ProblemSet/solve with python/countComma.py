n = int(input("Enter the number: "))
comma=0
if n<1000:
    comma=0
else:
    for i in range(1000,n+1):
        comma+=1
print(comma)

# class Solution:
#     def countCommas(self, n: int) -> int:
#         commas=0
#         x = 1000
#         while x<=n:
#             commas+= n-x+1
#             x*=1000
#         return commas
        