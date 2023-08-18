
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = collections.Counter(t)
        cur = collections.Counter()
        
        best = len(s)+1
        start = -1
        left = 0
        
        for r in range(len(s)):
            cur[s[r]] += 1
            
            while cur >= c:
                if r - left + 1 < best:
                    best = r - left + 1
                    start = left
                cur[s[left]]-=1
                left+=1
    
        return s[start:start+best] if start != -1 else ""
