class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
            
        # [-4,-1,-1,0,1,2]
        # a + b + c = 0
        # a = -b + - c
        # a = -(b+c)
        # -a = b + c
        # -i = j + k

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # if index is more than 0 & its value is 
            # equal to it's prev value then skip
            if i > 0 and a == nums[i-1]:
                continue

            # create Left and Right pointer
            left = i+1
            right = len(nums)-1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    # then continue searching for next pairs
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        # if same left number appears, continue the pointer to left
                        left += 1

        return res









