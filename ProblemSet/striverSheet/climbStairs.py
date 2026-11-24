class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# brute force
class Solution:
    def climbStairs(self, n):
        return self.solve(n)
    def solve(self,step:int)-> int:
        if step == 0:
            return 1
        if step<0:
            return 0
        oneStepJump = self.solve(step - 1)
        twoStepJump = self.solve(step - 2)
        return oneStepJump + twoStepJump
    