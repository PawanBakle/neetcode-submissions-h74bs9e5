class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
            elif res and nums[i] != target:
                break
            
        if len(res) == 1:
            return res*2
        return [res[0],res[-1]] if res else [-1,-1] 