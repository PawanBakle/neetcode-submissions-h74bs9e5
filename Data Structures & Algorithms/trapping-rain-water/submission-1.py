class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        lmax, rmax = 0,0 #to get max from left or right side

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            #once we get max height from either side
            # we choose to measure water level
            if lmax < rmax:
                res += lmax - height[l]
                l +=1
            else:
                res += rmax- height[r]
                r -=1
        return res