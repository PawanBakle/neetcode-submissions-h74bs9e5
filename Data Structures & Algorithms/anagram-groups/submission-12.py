from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## first i have to calculate and sort and store each 
        ## anagram sorted() in a dict with value = []
        if len(strs) == 1:
            return [strs]
        elif strs == "":
            return [[""]]
        sorted_anagram = {}
       
        for each_chars in strs:
            result_string = "".join(sorted(each_chars))
            if result_string not in sorted_anagram.keys():
                sorted_anagram[result_string] = []
        # now i have something like {cat= [], tops = []}
        # then loop through array and add if anagram exists

        for each_chars in strs:
            result_string = "".join(sorted(each_chars))
            # result_string = "".join(sorted(calci.keys()))

            if result_string in sorted_anagram.keys():
                sorted_anagram[result_string].append(each_chars)
        return list(sorted_anagram.values())

