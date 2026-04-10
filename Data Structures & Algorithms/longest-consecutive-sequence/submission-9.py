class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_maal = sorted(list(set(nums)))
        ct = 0
        result = []
        for i in range(len(sorted_maal)-1):
            if sorted_maal[i+1] - sorted_maal[i] == 1:
                ct += 1
                continue
            else:
                result.append(ct)
                ct = 0
                # return result + 1
        result.append(ct)
        if len(result) == 0:
            # result.append(ct)
        
            # l = max(result)
            # k = result[-1]
            return ct+1
        else:        
            l = max(result)
          
            return l+1