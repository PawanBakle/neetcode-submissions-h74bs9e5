class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        new_word = []
        while left < len(word1) or right < len(word2):
            if left < len(word1):
                new_word.append(word1[left])
            if right < len(word2):
                new_word.append(word2[right])
            left += 1
            right += 1
        return "".join(new_word)