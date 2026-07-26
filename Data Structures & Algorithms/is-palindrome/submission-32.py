import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # strip naked the string and check if first half is same as second half of the string
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_text = cleaned_text.lower()
        n = len(cleaned_text)

        i = 0
        j = -1
        while i < (n//2):
            if cleaned_text[i] != cleaned_text[j]:
                return False
            i += 1
            j -= 1
        return True
