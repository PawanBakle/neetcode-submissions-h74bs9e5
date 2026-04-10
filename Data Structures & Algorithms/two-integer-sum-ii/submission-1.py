class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return if there are only 2 elements
        if len(numbers) == 2:
            return [1,2]


        left_side = 0
        right_side = len(numbers) - 1

        # continue until left < right
        while left_side < right_side:
            sum2 = numbers[left_side] + numbers[right_side]
            # check if sum is more than target
            if sum2 > target:
                # means right element is bigger
                # reduce it
                right_side -= 1
            elif sum2 < target:
                left_side += 1
            else:
                return [left_side + 1,right_side + 1]


            