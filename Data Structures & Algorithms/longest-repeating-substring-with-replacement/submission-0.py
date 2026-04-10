class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        "check all the highest frequencies"

        high_freq = {}
        count = {}
        res = 0
        for i in range(len(s)):
            high_freq[s[i]] = 1 + high_freq.get(s[i],0)
        "high_freq = {A:4, B:3}"
        "the moment we replace other character with hF, we maximize the count"

        "like we check in the string if it's part of hF"
        "we keep expanding window"
        # c2e = high_freq.get(0)
        win = {}
        num_of_chars = len(s) - len(high_freq) # but why do we need that? 
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res



