class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        while right < len(nums):
            if left == right:
                right += 1
            elif nums[left] == nums[right]:
                # left += 1
                right += 1
            elif nums[left] != nums[right]:
                # if left > 0 and nums[left] == nums[left-1]:               
                left += 1
                nums[left] = nums[right]
                right += 1
                # else:
                #     left += 1
                #     right+=1 
        k = 0
        for i in range(1,left+1):
            if nums[i] != nums[i-1]:
                k += 1
            
                
        return k+1
