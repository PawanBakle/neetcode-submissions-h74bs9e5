class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## i feel brute force is just to check target exists?

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1