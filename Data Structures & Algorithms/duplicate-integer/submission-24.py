class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keep = {}
        for i in range(len(nums)):
            if nums[i] not in keep:
                keep[nums[i]] = i
            else:
                return True
            
        return False