
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer solution
        # sort the array first
        # for each element, find the other two elements that sum to 0
        # if the sum is less than 0, move the left pointer
        # if the sum is greater than 0, move the right pointer
        # 
        # Time complexity: O(n^2)
        # Space complexity: O(1)

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res.append(tuple([nums[j], nums[k], nums[i]]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return list(set(res))

