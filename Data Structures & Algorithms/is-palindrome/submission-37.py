import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = [c.lower() for c in s if c.isalnum()]
        if len(k) <= 1:
            return True
        if k[0] != k[-1]:
            return False
        return self.isPalindrome(k[1:-1]) 
        