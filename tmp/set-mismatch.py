
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        sum_set = sum(s)
        sum_all = sum(nums)
        dupl = sum_all-sum_set
        return [dupl, (((1+len(nums))*len(nums))//2)-sum_set]

