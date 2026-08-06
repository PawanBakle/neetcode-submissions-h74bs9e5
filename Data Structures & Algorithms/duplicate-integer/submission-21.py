class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # p = set(nums)
        # if len(p) == len(nums):
        #     return False
        # return True
        hashes = {}
        for i in range(len(nums)):
            if nums[i] not in hashes:
                hashes[nums[i]] = i
            else:
                return True
        return False