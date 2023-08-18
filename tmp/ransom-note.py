
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = collections.Counter(magazine)
        for n in ransomNote:
            if c[n] <= 0:
                return False
            c[n] -= 1
        return True
        


        
