class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_Compliment = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in check_Compliment.keys():
                if nums[i] + compliment == target:
                    # return [compliment,i]
                    return [check_Compliment[compliment],i]
            else:
                check_Compliment[nums[i]] = i
        