class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        # mid = len(nums) // 2
        # if len(nums) <= 1:
        #     return 1
        while left <= right:
            mid = (left + right) // 2
            # tar = nums[left] + nums[right]
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
            # else:
            #     break
        # if numsmid == target:
        #     return mid-1
        # else:
        return -1     