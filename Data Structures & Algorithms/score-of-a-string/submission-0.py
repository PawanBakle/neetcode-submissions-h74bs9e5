class Solution:
    def scoreOfString(self, s: str) -> int:
        # first we convert to ascii and store those numbers in an array
        # then in a loop compute the difference 
        # add those differences

        asci_val = list(map(ord,s))
        diff = []
        for i in range(1,len(asci_val)):
            dif = abs(asci_val[i] - asci_val[i-1])
            diff.append(dif)
        val = 0
        for i in range(len(diff)):
            val += diff[i]
        return val