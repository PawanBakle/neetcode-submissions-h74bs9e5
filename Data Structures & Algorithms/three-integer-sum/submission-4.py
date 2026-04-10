class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = len(nums) - 1
        t_res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            a = nums[i]
            left = i+1 
            right = len(nums) - 1
            while left < right:
                t_sum = a + nums[left] + nums[right]
                if t_sum < 0:
                    left += 1
                elif t_sum > 0:
                    right -= 1
                else:
                    t_res.append([a, nums[left],nums[right]])
                    left += 1
                    right -= 1
        # t_set = set(t_res)
        tuple_list = [tuple(item) for item in t_res]
        uniq = set(tuple_list)
        result_list = [list(item) for item in uniq]
         
        return result_list
                
