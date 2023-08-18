
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        result = 0
        for p in prices[1:]:
            mini = min(mini, p)
            result = max(result, p-mini)
        return result
        
