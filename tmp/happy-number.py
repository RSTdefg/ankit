
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            sumi = 0
            for c in str(n):
                sumi += int(c)*int(c)
            n = sumi
            if n in seen:
                return False
            seen.add(n)
        return True
            
                
            
        
