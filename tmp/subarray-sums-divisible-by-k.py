
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = collections.Counter()
        c[0] = 1
        result = 0
        sumi = 0
        for n in nums:
            sumi += n
            result += c[sumi%k]
            c[sumi%k] += 1
        return result
            
            

        
