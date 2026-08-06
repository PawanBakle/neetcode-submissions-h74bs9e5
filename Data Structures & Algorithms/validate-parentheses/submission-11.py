class Solution:
    def isValid(self, s: str) -> bool:
        c_bracks = {')':'(','}':'{',']':'['}
        stck = []
        if len(s) == 1:
            return False
        for chars in s:
            if chars not in c_bracks:
                stck.append(chars)
            else:
                if stck and stck[-1] == c_bracks[chars]:
                    stck.pop()
                else:
                    return False
        
        if len(stck) == 0:
            return True
        return False
