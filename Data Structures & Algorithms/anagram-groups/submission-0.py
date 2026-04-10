class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        # strs = ["act","pots","tops","cat","stop","hat"]
        # sort the element in the list
        for i in strs:
            store = ''.join(sorted(i))
            result[store].append(i)
        return list(result.values())