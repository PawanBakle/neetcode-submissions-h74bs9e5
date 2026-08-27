import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alpha-numeric character
        # loop till half of the string and check if first and last elements are same if not return False

        clean_str = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        left = 0
        right = len(clean_str)-1
        while left < right:
            if clean_str[left] != clean_str[right]:
                return False
            left += 1
            right -= 1
        return True