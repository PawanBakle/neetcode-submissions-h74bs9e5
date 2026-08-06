class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        'for current day, check rest of the days. if not dif= 0'

        res = [0]*len(t)
        stack = []
        for i_day, i_temp in enumerate(t):
            'we use stack to keep checking last temp not higher'
            while stack and i_temp > t[stack[-1]]:
                prev = stack.pop()
                res[prev] = i_day - prev
            
            'if not >, if store the cur days temp(i_pos) in the stack'
            stack.append(i_day)
        return res