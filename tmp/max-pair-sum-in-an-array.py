
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s1 = str(nums[i])
                s2 = str(nums[j])
                m1 = -1
                m2 = -1
                for c in s1:
                    m1 = max(m1, int(c))
                for c in s2:
                    m2 = max(m2, int(c))
                if m1 == m2:
                    maxi = max(maxi, nums[i]+nums[j])
                    
        return maxi
                
                
        
        
