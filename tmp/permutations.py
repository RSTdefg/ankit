
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append(nums)

        # def go(remain):
        #     cur = []
        #     for res in result:
        #         for i, rem in enumerate(remain):
        #             cur.append(res+[rem])
        def go(i, cur):
            if i >= len(cur):
                return
            go(i+1, cur)
            for j in range(i+1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                result.append(nums[::])
                go(i+1, nums[::])
                nums[i], nums[j] = nums[j], nums[i]
        go(0, nums)
        return result


