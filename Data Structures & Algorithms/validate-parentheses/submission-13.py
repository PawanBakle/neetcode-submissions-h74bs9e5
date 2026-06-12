class Solution:
    def isValid(self, s: str) -> bool:
        c_bracks = {')':'(','}':'{',']':'['}
        stck = []
        if len(s) == 1:
            return False
        for chars in s:
            if chars == '(':
                stck.append(')')
            elif chars == '[':
                stck.append(']')
            elif chars == '{':
                stck.append('}')
            else:
                if stck and stck[-1] == chars:
                    stck.pop()
                else:
                    # stack does not have last bracket
                    # maybe first element is closing bracket itself
                    return False
        if len(stck) == 0:
            return True

        return False
