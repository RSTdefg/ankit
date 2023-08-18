
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        li = []

        for num in nums:
            i = bisect_left(li, num)
            if i == len(li):
                li.append(num)
            else:
                li[i] = num

        return len(li)
