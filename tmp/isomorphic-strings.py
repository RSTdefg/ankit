
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        m2 = {}
        for c1, c2 in zip(s, t):
            if c2 in m and m[c2] != c1:
                return False
            if c1 in m2 and m2[c1] != c2:
                return False
            m[c2] = c1
            m2[c1] = c2
                
        return True
            
