class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1  #len(nums) -2 inclusive ([left, right])
        right = len(nums)     #arr = len(nums) -1 exclusive ([left, right))
        while left < right:

             # check till left > right
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # target is somewhere on the left side
                right = mid # to avoid loop& keep right as border
            else:
                left = mid + 1
        return -1