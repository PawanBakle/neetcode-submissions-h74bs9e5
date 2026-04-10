class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a = sorted(s)
        # b = sorted(t)
        if len(s) != len(t):
            return False
        # return False
        char_count = {}
        for i in s:
            if i not in char_count.keys():
                char_count[i] = 1
            else:
                char_count[i] += 1


        tar_count = {}
        for j in t:
            if j not in tar_count.keys():
                tar_count[j] = 1
            else:
                tar_count[j] += 1
        if char_count == tar_count:
            return True
        return False
        