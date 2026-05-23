class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        what we can do is. have 2 pointers. make right move if we find any dupicates


        '''
        l = 1
        for r in range(1, len(nums)):
            # check for duplicates
            if nums[r] != nums[r-1]:
                nums[l] = nums[r] # replace left value with right one and move on
                l += 1
        return l
