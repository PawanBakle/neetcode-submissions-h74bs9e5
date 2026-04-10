class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = defaultdict(list)
        result = {}
        # strs = ["act","pots","tops","cat","stop","hat"]
        # sort the element in the list
        for i in strs:
            store = ''.join(sorted(i))
            if not result.get(store,''):
                result[store] = []
                result[store].append(i)
            else:
                result[store].append(i)
        # return list(result.values())
        return list(result.values())