
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lhs, rhs = [1], [1]
        res = []
        for n in nums[:-1]:
            lhs.append(n*lhs[-1])
        for n in reversed(nums[1:]):
            rhs.append(n*rhs[-1])
        rhs.reverse()
        for i in range(len(nums)):
            res.append(lhs[i]*rhs[i])
        return res
        
        
