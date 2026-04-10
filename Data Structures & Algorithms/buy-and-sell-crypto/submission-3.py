class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        in order to find max profit , keep looking for prices at 
        left(buy) < right(sell) 
        '''

        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[right] >= prices[left]:
                dif = prices[right] - prices[left]
                max_profit = max(max_profit, dif)
            else:
                left = right
        return max_profit
