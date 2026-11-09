class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = float('-inf')
        for right in range(len(prices)):
            # first check the diff. 
            # if dif is positive move right 
            # if not or less move left
            result = prices[right] - prices[left]
            if result > 0:
                profit = max(profit,result)

            else:
                left = right
        if profit == float('-inf'):
            return 0
        return profit