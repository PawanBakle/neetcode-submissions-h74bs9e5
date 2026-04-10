class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mape = {}
        
        for i in range(len(nums)):
            num = mape.get(nums[i],None)
            if num == None:
                mape[nums[i]] = nums[i]
            else: 
                return True

        return False
        