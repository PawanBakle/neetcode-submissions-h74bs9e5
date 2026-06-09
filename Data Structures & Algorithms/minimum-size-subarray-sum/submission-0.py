class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curSum = 0
        last_len = float('inf')
        for right in range(len(nums)):
            # expand till sum matches the condition
            curSum += nums[right]
            while curSum >= target:
                # update the size
                last_len =min(last_len, right - left + 1)
                # remove the left element
                curSum -= nums[left]
                left += 1
        return 0 if last_len == float('inf') else last_len