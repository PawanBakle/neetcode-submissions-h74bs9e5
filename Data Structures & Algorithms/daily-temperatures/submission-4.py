class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        'for current day, check rest of the days. if not dif= 0'

        res = []
        for i in range(len(t)):
            'min days is 1'
            count = 1
            j = i+1
            while j < len(t):
                if t[j] > t[i]:
                    break
                
                count += 1
                j += 1
            count = 0 if j == len(t) else count # is j relevant after loop?
            res.append(count)  

        return res