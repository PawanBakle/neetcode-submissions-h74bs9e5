class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sums = defaultdict(int)
        for i in range(len(numbers)):
            tw_sums = target - numbers[i]
            if sums[tw_sums]:
                return [sums[tw_sums],i+1]
            else:
                sums[numbers[i]] = i+1