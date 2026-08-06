class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                # reassign the value since new val is found
                nums[left] = nums[right]
                left += 1

        return left

