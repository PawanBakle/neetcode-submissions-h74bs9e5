class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        clean_s= "".join(char for char in s if char.isalnum()).lower()

        # cut the string in half
        half = len(clean_s) //2
        first = 0
        last = len(clean_s) - 1
        if len(clean_s) == 0 or len(clean_s) == 1:
            return True
        while first < half:
            if clean_s[first] ==  clean_s[last]:
                first += 1
                last -= 1
            else: 
                return False
                
        return True


        