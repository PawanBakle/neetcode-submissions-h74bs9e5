class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i_am_present = {}

        for i in range(len(nums)):
            if nums[i] not in i_am_present.keys():
                i_am_present[nums[i]] = i
            else:
                return True
        return False
        