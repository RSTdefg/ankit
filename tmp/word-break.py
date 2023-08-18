
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def go(i):
            if i == len(s):
                return True
            res = False
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    res = res or go(j)
            return res
        return go(0)
            
                    
            

        
