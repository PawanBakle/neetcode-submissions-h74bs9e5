class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        # prices = [10,1,5,6,7,1]
        # prices = [10,8,7,5,2]
        maxi = -1 #4, #5, #6, | 
        left = 0 #1, | #1, #2, #3
        right = 1 #2, #3, #4, #5 | #2, #3, #4
        # for i in range(len(arr)):
        while right <= len(arr) -1:
            
            if arr[left] >= arr[right]:
                left = right
                right += 1
            # i need to find a way to check that right does not cross the array. how about while?  
            else:
                dif = arr[right] - arr[left]
                maxi = max(dif, maxi) 
                right +=1 
                # increment if diff found
        if maxi == -1:
            return 0
        return maxi