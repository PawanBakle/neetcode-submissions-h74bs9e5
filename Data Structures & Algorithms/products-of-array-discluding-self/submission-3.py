class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            arr.append(product)
        return arr