class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        brute force was just to check if num existed and if not then -1
        basically linear search
        There are two cases: l and mid belong to the left sorted segment, or mid and r belong to the right sorted segment. 
        If l and mid are in the same segment, nums[l] < nums[mid], so the pivot index must lie in the right part. 
        If mid and r are in the same segment, nums[mid] < nums[r],
        so the pivot index must lie in the left part. After the binary search, we eventually find the pivot index.
        Once the pivot is found, it's straightforward to select the segment where the target lies and perform a binary search on that segement to find its position.
        If we don't find the target, we return -1.
        """
        left = 0
        right = len(nums)-1
        pivot = 0
        while left < right:
                mid = (left+ right) // 2
                if nums[mid] > nums[right]:
                        left = mid + 1
                else: 
                        
                        right = mid 
        pivot = left
        left, right = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[right]:
                left = pivot
        else:
                right = pivot - 1

        while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                        return mid
                elif nums[mid] > target:
                        right = mid -1
                else:
                        left = mid + 1
        return -1 

        


