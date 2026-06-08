import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        elif num == 2:
            return False
        # for i in range(0, (num+1)//2):
        #     if i*i == num:
        #         return True
        # return False

        l = 0
        r = num
        while l <= r:
            mid = int(l + (r - l)/2)
            val = mid*mid
            if val == num:
                return True
            elif val > num:
                r = mid-1
            else:
                l = mid+1
        return False