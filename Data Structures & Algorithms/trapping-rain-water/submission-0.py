class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        First calculate the max that can hold between left and right
        Then if left is less than right
        Add the current water level to the answer

        else add current water level from right
        '''

        n = len(height)
        l = 0
        r = n-1
        res = 0
        lmax, rmax = 0,0
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax,height[r])
            if lmax < rmax:
                res += lmax - height[l]
                l +=1
            else:
                res += rmax - height[r]
                r -= 1

        return res