
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        rolling =  nums[0]
        maxi = rolling
        rolling = max(nums[0], 0)
        for n in nums[1:]:
            rolling += n
            maxi = max(maxi, rolling)
            if rolling < 0:
                rolling = 0
            
        return maxi


