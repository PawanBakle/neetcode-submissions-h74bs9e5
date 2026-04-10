class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkerBaby = {}
        for i in range(len(nums)):
            val = checkerBaby.get(nums[i],None)

            if val == None:
                checkerBaby[nums[i]] = nums[i]
            else:
                return True
        return False