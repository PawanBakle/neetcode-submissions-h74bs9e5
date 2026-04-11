class Solution:
    def dailyTemperatures(self, temperature: List[int]) -> List[int]:
        """ 
        day i, checking next, if not next, if not next till end of the day
        if not till end add 0 
        if find next j which is j > i then add the temp[j]
        """
        n = len(temperature)
        res = []
        for i in range(n):
            count = 1
            j = i+1 # check from next day uptill end
            while j < n:
                if temperature[j] > temperature[i]:
                    break
                # if not increment 1
                count += 1
                j += 1
            # if i don't get till n then add 0 or else add count
            count = 0 if j == n else count
            res.append(count)

        return res
