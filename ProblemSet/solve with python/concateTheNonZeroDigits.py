class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)      

        x = ""
        total = 0

        for ch in n:
            if ch == '0':
                continue

            x += ch
            total += int(ch)

        if x == "":
            return 0

        return total * int(x)
obj = Solution()
print(obj.sumAndMultiply(10203004)) 