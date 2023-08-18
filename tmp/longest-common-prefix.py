
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur = 0
        while True:
            for s in strs:
                if cur >= len(s) or s[cur] != strs[0][cur]:
                    return strs[0][:cur]
            cur += 1
