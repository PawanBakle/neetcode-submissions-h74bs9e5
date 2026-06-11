class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)
        # [left,right) boundary at right

        while left < right: # keeping the boundary
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # shift left Pointer
                left = mid + 1 # +1 to avoid inf loop
            else:
                right = mid # keeping the boundary for right
        return -1
