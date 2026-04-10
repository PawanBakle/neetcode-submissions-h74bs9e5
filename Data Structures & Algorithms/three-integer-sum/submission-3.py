class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # i gotta use 2 pointers
        # basically fix 1 pointer and check other 2 pointers
        # and add 'em to see if they get to 0

        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        res = []
        for i in range(len(nums)-1):
            l = i+1 
            r = len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1

                elif three_sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

        return list(set(tuple(item) for item in res))

        