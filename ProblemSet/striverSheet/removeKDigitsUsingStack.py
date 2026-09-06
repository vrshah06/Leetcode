class Solution:
    def removeKdigits(self,nums: str, k: int):
        stack = []
        for digit in nums:
            #pop the last digit from stack if it is greater than the current digit and k>0
            while k>0 and stack and stack[-1]>digit:
                stack.pop()
                k -= 1
            #push the current digit to stack
            stack.append(digit)
            #if more digits need to be removed, pop the last digit from stack
        while k>0 and stack:
            stack.pop()
            k -= 1
        if not stack:
            return "0"
        result = ""
        #adding the digits from stack to result
        while stack:
            result += stack.pop()
        result = result.rstrip("0")
        result = result[::-1]
        if not result:
            return "0"
        return result
if __name__ == "__main__":
    nums = input("Enter the number as a string: ")
    k = int(input("Enter the number of digits to remove: "))
    solution = Solution()
    result = solution.removeKdigits(nums, k)
    print("The smallest number after removing", k, "digits is:", result)            