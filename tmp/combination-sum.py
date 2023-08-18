
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def go(sofar, sumi, i):
            if sumi > target:
                return
            if sumi == target:
                res.append(sofar)
                return
            if i >= len(candidates):
                return
            go(sofar+[candidates[i]], sumi+candidates[i], i)
            go(sofar, sumi, i+1)
            return
        go([], 0, 0)
        return res

