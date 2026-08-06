class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) 
        while left < right:
                # since right is exclusive [left,right)
                # we make sure in every interation we have right has wall(not included)
                mid = (left + right) // 2
                if nums[mid] == target:

                        return mid
                elif nums[mid] > target:
                        right = mid # make sure it's still exclusive
                else:
                        left = mid + 1
        return -1