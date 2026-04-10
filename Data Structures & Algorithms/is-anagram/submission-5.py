class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False
        s_map = {}
        for i in s:
                if i in s_map.keys():
                        s_map[i] += 1
                else:
                        s_map[i] = 1
        t_map = {}
        for i in t:
                if i in t_map.keys():
                        t_map[i] += 1
                else:
                        t_map[i] = 1
        s_sort = dict(sorted(s_map.items(), key=lambda item: item[1]))
        t_sort = dict(sorted(t_map.items(), key=lambda item: item[1]))
        if s_sort == t_sort:
                return True
        else:
                return False



