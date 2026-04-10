class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
                return 0
        left = 0
        # right = 0
        max_len = {}
        maxy = 0
        for right in range(len(s)):
                if s[right] in max_len and max_len[s[right]] >= left:
                     # basically reset left's position
                        left = max_len[s[right]] + 1
               
                # increment right pointer
                max_len[s[right]] = right
                maxy = max(maxy, right -left +1)
        return maxy 
                     
                
                