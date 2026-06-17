from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a hashmap to store both and compare
        # s = Counter(s)
        result_s = "".join(sorted(s))
        # t = Counter(t)
        result_t = "".join(sorted(t))
        if result_s == result_t:
            return True
        return False

        