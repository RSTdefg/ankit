
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def act(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            if buy:
                memo[(i, buy)] = max(act(i+1, False)-prices[i], act(i+1, True))
            else:
                memo[(i, buy)] = max(act(i+2, True)+prices[i], act(i+1, False))
            return memo[(i, buy)]
        
        res = act(0, True)
        return res
                     
