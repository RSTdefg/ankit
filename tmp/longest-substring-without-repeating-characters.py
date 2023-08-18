
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        dict = set()
        for r in range(len(s)):
            if s[r] in dict:
                while l < r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    dict.remove(s[l])
                    l += 1
            dict.add(s[r])
            result = max(result, r - l + 1)
        return result
            


        
