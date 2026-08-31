class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        new_work = ''
        while left < len(word1) and right < len(word2):
            new_work = new_work + word1[left] 
            new_work = new_work + word2[right]
            left += 1
            right += 1

        while left < len(word1):
            new_work = new_work + word1[left] 
            left += 1

        while right < len(word2):
            new_work = new_work + word2[right] 
            right += 1
        return new_work