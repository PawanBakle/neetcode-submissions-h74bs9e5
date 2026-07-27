class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) 

        # why won't this work???
        while left < right: # wall
            mid = (left + right) //2
            if nums[mid] > target:
                right = mid # already at the wall
                # right = mid-1 will comes inside wall and left< right will skip the last element
            elif nums[mid] < target:
                left = mid+ 1
            elif nums[mid] == target:
                return mid
        return -1