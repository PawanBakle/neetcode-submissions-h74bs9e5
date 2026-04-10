class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #assign first number
        #then loop through rest using 2 pointers

        numss = sorted(nums)
        tripsi = []
        p1 = 0
        r = len(numss)-1
        l = 0
        for i in range(len(numss)-1):
            p1 = numss[i]
            r = len(numss)-1
            l = i+1
            # first check if p1 ==  l
            while l < r:

                # if p1 == l:
                #     l += 1 
                # if p1 == r:
                #     r -= 1
                t_sum = numss[i] + numss[l] + numss[r]
                if t_sum == 0:
                    tripsi.append([p1,numss[l],numss[r]])
                    l += 1
                    r -= 1
                elif t_sum < 0:
                    l += 1
                elif t_sum > 0:
                    r -= 1

        return list(set(tuple(item) for item in tripsi))