class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ct = 0
        n = len(details) 
        for i in range(n):
            if int(details[i][11:13]) > 60:
                ct += 1
        return ct