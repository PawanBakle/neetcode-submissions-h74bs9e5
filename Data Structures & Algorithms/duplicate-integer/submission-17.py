class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fDupl = {}
        lnum = sorted(nums)
        for i in range(len(lnum)):
            val = fDupl.get(lnum[i],None)
            if val != None:
                return True
            else:
                fDupl[lnum[i]] = lnum[i]

        return False
        