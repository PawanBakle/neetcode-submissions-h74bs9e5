class Solution:
    def validPalindrome(self, s: str) -> bool:
        left_side = 0
        right_side = len(s) - 1
        c = 0 
        while left_side < right_side:
            if c > 1:
                return False
            if s[left_side] == s[right_side]:
                left_side += 1
                right_side -= 1
            else:
                # OPTIMIZATION: Instead of a counter 'c', upon the first mismatch,
                # check the two possible resulting substrings. 
                # This is the only time a choice needs to be made.
                opt1 = s[left_side + 1 : right_side + 1]
                opt2 = s[left_side : right_side]
                return opt1 == opt1[::-1] or opt2 == opt2[::-1]
            # elif s[left_side] != s[right_side] :
            #     c +=1 
            #     left_side += 1 
            # elif s[right_side] != s[left_side]:
            #     c += 1
            #     right_side -= 1 
        return True



