class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        -> array of integers are given [x,x,x,x]
        -> return longest consecutive which can be formed
        -> What is longest consecutive seq? - sequence of elements 
        where each element is exactly 1 greater than previous

        '''
    #[9,1,4,7,3,-1,0,5,8,-1,6]
    #[-1,-1,0,1,3,4,5,6,7,8,9]

        largest_count = []
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                largest_count.append(count)
                count = 1
        largest_count.append(count)
        return max(largest_count) 