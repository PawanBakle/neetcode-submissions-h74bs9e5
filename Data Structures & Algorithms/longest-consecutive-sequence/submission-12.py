class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # sort the array/
        # have a counter to check if prev = cur -1 
        # for same just continue
        # for diff just continue

        arr = sorted(nums)
        counter = 0
        max_count = float('-inf')
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                continue
            # mistake 1  diff = arr[i-1] - arr[i]
            diff = arr[i] - arr[i-1]
            # mistake 2 if i == i-1:
            if diff == 1:
                counter += 1
                max_count = max(max_count, counter)
            elif diff > 1:
                max_count = max(max_count, counter)
                counter = 0
        if max_count == float('-inf'): # mistake 3 did not think about if all vals are same
            return 1
        return max_count + 1