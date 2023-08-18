
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li = s.split()
        if len(li) != len(pattern):
            return False
        m1 = {}
        m2 = {}
        for c, st in zip(pattern, li):
            if c in m1 and m1[c] != st:
                return False
            if st in m2 and m2[st] != c:
                return False
            m1[c] = st
            m2[st] = c
        return True
        
