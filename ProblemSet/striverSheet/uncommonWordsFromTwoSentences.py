class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = (s1+" "+s2).split()
        seen = {}
        for word in ans:
            if word in seen:
                seen[word]+=1 
            else:
                seen[word]=1 
        
        res = []
        for key,val in seen.items():
            if val == 1:
                res.append(key)
        
        return res

        