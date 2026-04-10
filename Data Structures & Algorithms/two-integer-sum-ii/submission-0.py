class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        if len(numbers) == 2:
            return [1,2]
        for i in range(len(numbers)):
            while left < right:
                sumit = numbers[left]+numbers[right]
                if sumit == target:
                    return [left+1, right+1]
                elif sumit < target:
                    left += 1
                elif sumit > target:
                    right -= 1
        