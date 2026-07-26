class Solution:
    def isValid(self, s: str) -> bool:
        '''one which first gets opened need to be closed first'''
        #store closed ones and check if it occurs .. when it does pop out open 
        closed_bracs = {'}':'{',']':'[',')':'('}
        stck = []
        
        for i in range(len(s)):
            if s[i] not in closed_bracs:
                stck.append(s[i])
            else:
                if stck and closed_bracs[s[i]] == stck[-1]:
                    stck.pop()
                else:
                    return False
        if not stck:
            return True
        return False 