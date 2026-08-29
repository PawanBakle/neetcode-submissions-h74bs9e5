class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stck = {}
        max_len = 0
        exp_len = 1
        l,r = 0,0
        n = len(s)
        while r < n:
            while s[r] in stck:
                # stck.pop(0)
                del stck[s[l]]
                l +=1
                exp_len -= 1
            # stck.append(s[i])
            stck[s[r]]= stck.get(s[r], 0) + 1
            max_len = max(exp_len, max_len)
            exp_len+=1
            r += 1
            # if s[i] not in stck:
            # stck.append(s[i])
            #     # stck[s[i]] += 1
            # exp_len += 1
            # max_len = max(exp_len, max_len)



        return max_len
        