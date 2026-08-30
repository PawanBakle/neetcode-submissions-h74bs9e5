class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        exp_len = 0
        cur_sum = float('inf')
        n = len(nums)
        for right in range(n):
            exp_len += nums[right]
            while exp_len >= target:
                cur_sum = min(right-left+1,cur_sum)
                exp_len -= nums[left]
                left += 1
        if cur_sum == float('inf'):
            return 0
        return cur_sum