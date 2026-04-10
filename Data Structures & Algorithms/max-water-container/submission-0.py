class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        # for l in range(len(heights)):
        #     for r in range(l+1,len(heights)):
        #         area = max(res,((r-l)*min(heights[l],heights[r])))
        #         # res = max(res,area)
        # return area
        while l< r:
            area = ((r-l)*min(heights[l],heights[r]))
            res = max(area,res)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
        return res
