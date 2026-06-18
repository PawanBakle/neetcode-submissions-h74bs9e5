class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums) 
        suffix = [1]*len(nums) 
        arr = [1]*len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1,len(nums)):
            prefix[i] = nums[i]* prefix[i-1]
        
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = suffix[j+1]* nums[j]
        arr[0] = suffix[1]
        
        for k in range(1,len(arr)-1):
            arr[k] = prefix[k-1]*suffix[k+1]
        arr[-1] = prefix[-2]
        return arr