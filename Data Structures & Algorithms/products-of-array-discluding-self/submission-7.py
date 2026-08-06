class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return arr
        
        # arr = [1, 2,3,4,5]
        # i  want something like [1,3,6,10,15]
        # assign first value
        prefix_shit = [1]*len(arr)
        prefix_shit[0] = arr[0]

        for i in range(1, len(arr)):
            prefix_shit[i] = prefix_shit[i-1] * arr[i]
            
        # similar goes for suffix_sum
       
        suffix_shit = [1]*len(arr)
        # i want something like [15,14,12,9,5]
        suffix_shit[-1] = arr[-1]
        for j in range(len(arr)-2,-1,-1):
            # we begin from second last element 
            suffix_shit[j] = suffix_shit[j+1]*arr[j]

        '''
        so for question asking product except self. we need for product for every element except self
        so basically arr[element] = prefix[element - 1]*suffix[element+1]

        exceptions occur for first and last element because for first element it's just suffix[element+1] and for last it's just prefix[element-1]
        '''
        
        self_arr = [1]*len(arr)
        for ele in range(len(arr)):
            if ele == 0:
                self_arr[ele] = suffix_shit[ele+1]
            elif ele == len(arr)-1:
                self_arr[ele] = prefix_shit[ele-1]
            
            else:
                self_arr[ele] = prefix_shit[ele-1]*suffix_shit[ele+1]

        return self_arr