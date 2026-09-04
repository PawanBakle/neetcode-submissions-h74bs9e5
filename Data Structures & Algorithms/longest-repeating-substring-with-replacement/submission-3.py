class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        check = {}
        res = 0
        for right in range(len(s)):
            check[s[right]] = check.get(s[right], 0) + 1
            max_freq = max(check[s[right]],max_freq)
            while (right-left+1) - max_freq > k:
                check[s[left]] -= 1
                left += 1
            res = max(res, (right - left + 1))
        return res