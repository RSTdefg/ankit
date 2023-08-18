
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def go(cur, i):
            if cur > amount or i >= len(coins):
                return 0
            if cur == amount:
                return 1
            sumi = 0
            sumi+=go(cur+coins[i], i)
            sumi+=go(cur, i+1)
            return sumi
        
        return go(0, 0)

