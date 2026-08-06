class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        sort the list
        then run a loop to check which elements have diff = 1
        have a max-len to check which series is longer
        '''
        sorted_nums = sorted(nums)
        max_len = float('-inf')
        max_dif = 0
        if len(sorted_nums) == 0:
            return 0
        elif len(sorted_nums) == 1:
            return 1
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i-1] == 1:
                max_dif += 1
                max_len = max(max_len, max_dif)
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                max_len = max(max_len, max_dif)
                max_dif = 0
        if max_len == float('-inf'):
            return 1
        return max_len+1