class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # loop through 
        # for every element find greatest towards right and replace it
        # return arr
        
        for i in range(len(arr)):
            greater_ele = float('-inf')
            ct = i+1
            if i == len(arr)-1:
                arr[i] = -1
                return arr
            while ct <= len(arr)-1:
                greater_ele = max(greater_ele,arr[ct])
                ct += 1
            
            arr[i] = greater_ele
        return arr