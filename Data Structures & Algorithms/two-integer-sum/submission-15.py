class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_hash = {}
        for i in range(len(nums)):
            comple = target - nums[i]
            c_hash = n_hash.get(comple,None)
            if c_hash is not None:
                return [n_hash[comple],i]
            n_hash[nums[i]] = i
        return []