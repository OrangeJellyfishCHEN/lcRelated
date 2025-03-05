from typing import List
class LC714:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l_p = len(prices)
        dp = [[0, 0] for _ in range(l_p)]
        dp[0][1] = -prices[0]
        for i in range(1, l_p):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return max(dp[l_p - 1][0], dp[l_p - 1][1])

