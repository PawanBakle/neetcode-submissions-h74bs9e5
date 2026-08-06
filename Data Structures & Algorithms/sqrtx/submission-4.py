class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 0, x+1
        while left < right:
            mid = ((left + right) // 2) + 1
            if mid*mid == x:
                return mid
            if mid*mid > x:
                right = mid - 1
            else:
                left = mid
        return left
        # if x == 0 or x == 1:
        #     return x
        # for i in range(0, ((x+1)//2)+1):
        #     if i*i == x:
        #         return i
        #     elif i*i > x:
        #         return i - 1
        