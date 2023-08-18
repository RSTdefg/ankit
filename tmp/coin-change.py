
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount+1)

        for i in range(1, amount+1):
            mini = float('inf')
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    mini = min(mini, 1+dp[i - coins[j]])
            dp[i] = mini
        
        return dp[-1] if dp[-1] != float('inf') else -1



