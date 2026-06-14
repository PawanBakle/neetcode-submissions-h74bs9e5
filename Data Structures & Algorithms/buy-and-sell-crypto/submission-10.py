class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0
        max_profit = float('-inf')
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
            # positive number and we can like perform diff
                dif = prices[right] - prices[left]
                max_profit = max(max_profit, dif)
                right += 1

            else:
                # if not shift the days to find next lower buy day
                left = right
                right += 1

        return 0 if max_profit == float('-inf') else max_profit