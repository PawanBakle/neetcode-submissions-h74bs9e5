class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # naive way to solve this
        left = 0
        right = len(s) - 1
        if len(s) == 1:
            return s
        
        while left < right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -=1 
        return s