class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        maps = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in maps:
                if not stk:
                    return False # no brackets stored
                if stk[-1] != maps[char]:
                    return False
                else:
                    stk.pop()
            # if char not in stk:
            #     if char not in maps:
            #         return False
            # if maps[char] == char:
                
            #     stk.pop(char)
            else:
                stk.append(char)
        if len(stk) == 0:
            return True
        return False