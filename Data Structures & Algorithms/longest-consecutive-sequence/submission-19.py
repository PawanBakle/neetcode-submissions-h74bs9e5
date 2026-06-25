class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        check if cur element is first in row
            if yes check for next consecutive cur+1s
        if cur element is not the first one 
            move next
        '''
        max_sum = float('-inf')
        
        set_nums = set(nums)
        for num in set_nums:
            if (num - 1) not in set_nums: # if element's prev does not exist (it's starting in the Line)
                streak = 1
                curNum = num 
                
                while curNum+1 in set_nums:
                    # as long as next exists keep updating streak
                    streak+=1
                    curNum +=1
                max_sum = max(max_sum, streak)
        return 0 if max_sum == float('-inf') else max_sum