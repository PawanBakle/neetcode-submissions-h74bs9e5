class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use compliment
        # what do i need to store? 
        # check if compliment exists in dict or not if not store the index 
        keep = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            # val = keep.get(comp, None)
            if comp in keep:
                return [keep[comp],i]
            else:
                keep[nums[i]] = i