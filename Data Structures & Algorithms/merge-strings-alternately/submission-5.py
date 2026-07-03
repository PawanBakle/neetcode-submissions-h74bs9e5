

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        # as long as the pointers are less than word's len
        # keep adding

        newWord = ''
        w1_pointer = 0
        w2_pointer = 0
        word1_len = len(word1)
        word2_len = len(word2) 
        while w1_pointer < word1_len and w2_pointer < word2_len:
            newWord =  newWord+word1[w1_pointer]
            newWord = newWord+word2[w2_pointer]
            w1_pointer += 1  
            w2_pointer += 1
        if w1_pointer <= word1_len-1:
            newWord = newWord + word1[w1_pointer:]
        else:
            newWord = newWord + word2[w2_pointer:]
        return newWord
