class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right: # since right is inclusive here
                mid = (left + right) // 2
                if nums[mid] == target:
                        return mid
                elif nums[mid] < target:
                        left = mid + 1 # we don't want to keep coming back to same left pointer thus, + 1
                else:
                        right = mid - 1 # we don't wanna keep coming back to same right thus -1

        return -1