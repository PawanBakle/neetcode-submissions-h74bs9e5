class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0
        max_1s = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ct += 1
                # max_1s = max(max_1s, ct)
            else:
                max_1s = max(max_1s, ct)
                ct = 0
        max_1s = max(max_1s, ct)
        return max_1s