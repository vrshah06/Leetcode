class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        count=0
        vow=['a','e','i','o','u']
        for i in range(len(s)-1,-1,-1):
            if s[i] in vow:
                count+=1
            else:
                break
        return s[:len(s)-count]