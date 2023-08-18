
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            mid = l + (r-l) // 2
            i, cnt = 0, 0
            while i < len(nums) -1:
                if nums[i+1] - nums[i] <= mid:
                    cnt += 1
                    i += 1
                i += 1
            if cnt < p:
                l = mid + 1
            else:
                r = mid - 1

        return l



            


