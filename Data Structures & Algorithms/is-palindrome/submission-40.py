class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove the space/ alphanumeric
        # in a loop from 0 - s/2 check if s[0] = s[-1]
        # if not exit.

        s = "".join(c.lower() for c in s if c.isalnum())

        i,j = 0,len(s)-1
        while i < len(s)//2:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True