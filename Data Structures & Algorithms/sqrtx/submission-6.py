class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        left = 0
        right = x + 1
        while left < right:
            mid = (( left +  right ) // 2 ) + 1
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid - 1
            else:
                # mid * mid < x
                left = mid 
        return left
