
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = {}
        maxi = 1
        for n in arr:
            if n - difference in m:
                m[n] = 1 + m[n-difference]
                maxi = max(maxi, m[n])
            else:
                m[n] = 1
        return maxi




