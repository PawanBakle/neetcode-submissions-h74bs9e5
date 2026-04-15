class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target: # without = target will never be reached 
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return right
        return right