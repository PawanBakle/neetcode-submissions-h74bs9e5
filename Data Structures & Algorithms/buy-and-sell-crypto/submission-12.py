class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # well it ain't complicated as it looks like
        left = 0
        right = 1
        max_prof = float('-inf')
        while right <= len(prices)-1:
            profit = prices[right] - prices[left]
            if profit > 0:
                max_prof = max(profit, max_prof)
                right += 1
            else:
                left = right
                right += 1
        if max_prof == float('-inf'):
            return 0
        return max_prof