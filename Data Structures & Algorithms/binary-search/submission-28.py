class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1 
        # [left,right] boundary at right (including right)

        while left <= right: # keeping the boundary
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # shift left Pointer
                left = mid + 1 # +1 to avoid inf loop
            else:
                right = mid -1 # since right is inclusive (if not mid can cause inf)
        return -1
