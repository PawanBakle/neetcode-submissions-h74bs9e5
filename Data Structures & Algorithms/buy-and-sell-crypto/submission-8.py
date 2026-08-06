class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = float('-inf')
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                pricy = prices[right] - prices[left]
                # left+=1
                max_prof = max(max_prof, pricy)
                right += 1
            else:
                left = right
                right += 1
        return 0 if max_prof == float('-inf') else max_prof

