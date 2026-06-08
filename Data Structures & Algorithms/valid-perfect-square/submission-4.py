import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(0, (num+1)//2):
            if i*i == num:
                return True
        return False