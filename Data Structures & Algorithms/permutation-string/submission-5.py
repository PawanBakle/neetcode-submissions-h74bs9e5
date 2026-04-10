class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        to check permutations for s2 inside s1
        compare the s2 window (of size s1)
        """
        if len(s2) < len(s1):
            return False
        s1_win, s2_win = {},{}
        for i in range(len(s1)):
            # insert values of s1 AND s2
            s1_win[s1[i]] = 1 + s1_win.get(s1[i],0)
            s2_win[s2[i]] = 1 + s2_win.get(s2[i],0)
        if s1_win == s2_win:
            return True
        left = 0
        for right in range(len(s1), len(s2)):
            # increment by adding right
            s2_win[s2[right]] = 1 + s2_win.get(s2[right],0)
            #decrement by removing left, moving window forward
            s2_win[s2[left]] -= 1
            if s2_win[s2[left]] == 0:
                s2_win.pop(s2[left])
            left += 1
            if s2_win == s1_win:
                return True
        return False