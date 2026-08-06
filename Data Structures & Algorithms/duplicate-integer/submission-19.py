class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        p = set(nums)
        if len(p) == len(nums):
            return False
        return True