class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]*len(t)
        stack = []
        for i_day, i_temp in enumerate(t):
            while stack and i_temp > t[stack[-1]]:
                prev = stack.pop()
                res[prev] = i_day - prev
            stack.append(i_day)
        return res