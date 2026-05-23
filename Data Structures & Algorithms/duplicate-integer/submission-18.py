class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupls = {}
        for i in range(len(nums)):
            if nums[i] not in dupls:
                dupls[nums[i]] = i

            else:
                return True
        return False        