class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers)-1

        for i in range(len(numbers)):
            t_sum = numbers[left] + numbers[right]
            if t_sum < target:
                left += 1
            elif t_sum > target:
                right -= 1
            else:

                return [left+1, right+1]