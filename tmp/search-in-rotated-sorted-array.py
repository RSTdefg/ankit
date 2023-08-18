
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        

        shift = l
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[(mid+shift)%len(nums)] == target:
                return (mid+shift)%len(nums)
            elif nums[(mid+shift)%len(nums)] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
            
