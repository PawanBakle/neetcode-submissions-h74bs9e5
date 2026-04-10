class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0


        while l < r:
            # we apply the formula of rect 
            app = ((r - l)*min(heights[r],heights[l]))
            res = max(app, res)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1

        return res