class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        searched = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    searched.append(words[i])
        return list(set(searched))