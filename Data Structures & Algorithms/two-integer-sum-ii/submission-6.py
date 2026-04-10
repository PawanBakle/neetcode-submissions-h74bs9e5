class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        '''
        we need to calculate compliment of 1 index
        num[i1] = target - num[i2]
        and we store 1 index inside hash as a key
        because comp is actually the other value
        '''

        two_sum = {}
        for i in range(len(numbers)):
            #find the complement of current element
            comp = target - numbers[i]
            val = two_sum.get(comp, None)
            if val is None:
                two_sum[numbers[i]] = i
                
            else:
                get_val = two_sum.get(comp,0)
                return [get_val+1, i+1]
            
