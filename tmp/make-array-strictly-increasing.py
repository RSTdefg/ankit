
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        memo = {}
        inf = float('inf')
        def make(i, prev):
            if i >= len(arr1):
                return 0
            
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            change = inf
            
            if arr1[i] > prev:
                change = min(change, make(i+1, arr1[i]))
            
            nextLarge = bisect.bisect_right(arr2, prev)
            if nextLarge != len(arr2):
                change = min(change, 1 + make(i+1, arr2[nextLarge]))
            
            memo[(i, prev)] = change
            return change
        
        res = make(0, -1)
        return res if res != inf else -1





        
