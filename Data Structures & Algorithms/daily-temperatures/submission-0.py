class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        count = 1
        l = len(temperatures)
        for i in range(len(temperatures)):
            j = i + 1
            # count = 1
            # for j in range(i+1, len(temperatures)):
            while j < l:
                if temperatures[j] > temperatures[i]:
                    # if i == 0:
                    #     res.append(count+1)
                    # else:
                    
                    # res.append(count)
                    # count = 1
                    break
                
                # elif j == len(temperatures)-1:
                #     count = 1
                #     res.append(0)

                j +=1
                count += 1
                
                
            count = 0 if j == len(temperatures) else count
            res.append(count)
            count = 1
            
                    
        return res