
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def go(i, j):
            print(i, j)
            if i == len(s1) and j == len(s2) and i+j == len(s3):
                return True
            if i + j >= len(s3):
                return False
            res = False
            if i < len(s1) and s1[i] == s3[i+j]:
                res = res or go(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]:
                res = res or go(i, j+1)            
            return res
        
        return go(0, 0)



