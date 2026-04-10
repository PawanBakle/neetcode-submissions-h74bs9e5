class Solution:
    def trap(self, height: List[int]) -> int:
        # need to calculate height 
        # left side max since water can get pured down from left
        # max side from either side for max water 

        res = 0
        lmax, rmax = 0,0
        l = 0
        r = len(height) - 1

        while l < r:
            lmax = max(lmax , height[l])
            rmax = max(rmax , height[r])
            if lmax < rmax:
                res += lmax - height[l]
                l += 1
            else:
                res += rmax - height[r]
                r -= 1
        return res
