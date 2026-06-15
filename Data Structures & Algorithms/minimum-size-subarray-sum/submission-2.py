class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        sumWin,diff = 0,0
        l = 0
        for r in range(len(nums)):
            sumWin += nums[r]
        # check condition
            while sumWin >= target:
                diff = r - l + 1
                sumWin -= nums[l]
                l += 1
                min_len = min(min_len, diff)
        # min_len = min(min_len, diff)
        if min_len == float('inf'):
            return 0
        return min_len