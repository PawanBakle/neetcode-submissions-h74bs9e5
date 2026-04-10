class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # so basically find the complement, save it as value as the 
        # key index of current array

        checkerBabes = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            # if checkerBabes[nums[i]] = complement:
            # val = checkerBabes.get(nums[i],0)
            if complement in checkerBabes:
                # if target == nums[i] + complement:
                return [checkerBabes[complement],i]
            # if target == nums[i] + complement:
            #     return [i,complement]
            checkerBabes[nums[i]] = i
                
        return 9