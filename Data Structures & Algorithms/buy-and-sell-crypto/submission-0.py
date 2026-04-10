class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        m_profit = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                m_profit = max(m_profit, profit)
            else:
                l = r
                r += 1
        return m_profit