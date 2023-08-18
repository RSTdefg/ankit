
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10**5]*len(nums)
        def go(index):
            if index >= len(nums) - 1:
                return 0
            if dp[index] != 10**5:
                return dp[index]
            for i in range(1, nums[index]+1):
                dp[index] = min(dp[index], 1+go(index+i))
            return dp[index]
        return go(0)
