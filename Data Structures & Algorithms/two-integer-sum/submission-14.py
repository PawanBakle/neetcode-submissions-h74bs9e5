class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find complement 
        num_com = {}
        for i in range(len(nums)):
                comp = target - nums[i]
                if num_com.get(comp,None) == None:
                        num_com[nums[i]] = i
                else:
                        return [num_com[comp],i]
        