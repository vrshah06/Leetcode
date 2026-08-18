c = int(input("Enter the number :"))
sqr = 0
for i in range(1,c+1):
    if i*i<=c:
        sqr=i
    else:
        break
print(sqr)
sum = sqr*sqr
for i in range(sqr+1):
    sum+=i*i
    if sum==c:
        print(True)
    else:
        sum= sqr*sqr
print(False)

#Method 2
from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):  # Iterate through all possible values of `a`
            b = sqrt(c - a * a)  # Compute `b` as the square root of `c - a^2`
            if b == int(b):  # Check if `b` is an integer
                return True  # If `b` is an integer, return true
        return False  # If no such pair `(a, b)` is found, return false