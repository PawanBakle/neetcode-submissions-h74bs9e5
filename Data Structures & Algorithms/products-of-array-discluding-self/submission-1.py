class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            a = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    a *= nums[j]   
            output.append(a)
        return output