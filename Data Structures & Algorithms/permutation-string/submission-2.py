class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_check,p_check = {},{}
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            s_check[s1[i]] = 1 + s_check.get(s1[i],0)
            p_check[s2[i]] = 1 + p_check.get(s2[i],0)
        "s_check = {l:1, e:1,c: 1}"
        "p_check = {a:1, b:1,c: 1}"
        if s_check == p_check:
            return True
        left = 0
        for right in range(len(s1),len(s2)): 
            p_check[s2[right]] = 1 + p_check.get(s2[right],0)
            p_check[s2[left]] -= 1  
            if p_check[s2[left]] == 0:
                p_check.pop(s2[left])
            # left += 1
            if p_check == s_check:
                return True
            left += 1
        return False