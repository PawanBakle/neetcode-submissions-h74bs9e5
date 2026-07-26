class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            # is_seen = seen.get(complement,None)
            if complement in seen:
                is_seen = seen.get(complement,None)
                return [is_seen,i]
            seen[nums[i]] = i
        