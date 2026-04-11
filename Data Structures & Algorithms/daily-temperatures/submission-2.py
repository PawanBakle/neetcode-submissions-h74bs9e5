class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        BASICALLY check for last temp less than current
        and if found, replace the last less temp's postion with dif
        """
        res = [0]*len(temperatures) # to store temperatures
        stack = []
        for cur_day,cur_temp in enumerate(temperatures):
            while stack and cur_temp > temperatures[stack[-1]]:
                'till last cur temp is greater than last stored'
                prev_day = stack.pop()
                res[prev_day] = cur_day - prev_day
            stack.append(cur_day)
        return res