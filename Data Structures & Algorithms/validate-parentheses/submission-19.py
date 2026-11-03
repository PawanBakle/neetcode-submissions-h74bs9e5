class Solution:
    def isValid(self, s: str) -> bool:
        keep = {')':'(','}':'{',']':'['}
        record = []
        for i in range(len(s)):
            if s[i] not in keep:
                record.append(s[i])
            else:
                if record and record[-1] == keep[s[i]]:
                    record.pop()

                else:
                    return False
        if len(record) == 0:
            return True
        return False