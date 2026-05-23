import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        ''' remove all the alphas and then loop till half 
        to check if vals are same from both ends
        '''
        cleaned_s = re.sub(r'\W', '', s).lower()

        left = 0
        right = len(cleaned_s)-1
        half = (len(cleaned_s))//2
        for i in range(0,half):
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -=1
        return True
