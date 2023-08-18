
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for _ in range(len(s))]

        def get(l, r):
            print(l, r)
            result = ""
            while l >=0 and r < len(s) and s[l]==s[r]:
                result = s[l:r+1]
                l, r = l-1, r+1
            return result
        res = ""
        for i in range(len(s)):
            s1, s2 = get(i, i), get(i, i+1)
            ns = s1 if len(s1) > len(s2) else s2
            res = ns if len(ns) > len(res) else res

        return res
            
                
        



