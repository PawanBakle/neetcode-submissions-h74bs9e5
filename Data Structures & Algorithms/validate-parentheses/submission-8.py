class Solution:
    def isValid(self, s: str) -> bool:
        s_map = {')':'(','}':'{',']':'['}
        stck = []
        # so keep storing the bracket as long as you don't find it in the s_map
        # if found pop
        if len(s) == 1:
            return False
        for i in s:
            get_b = s_map.get(i,None)
            if get_b not in stck:
                stck.append(i)
            else:
                # last stack == get_b 
                if stck and stck[-1] == s_map[i]:
                    stck.pop()
                else:
                    break
                # else:
                #     return False
        if stck:
            return False
        return True
                