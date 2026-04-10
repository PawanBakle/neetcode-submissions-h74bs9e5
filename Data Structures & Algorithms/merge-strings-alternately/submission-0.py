

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        # as long as the pointers are less than word's len
        # keep adding

        newWord = ''

        w1_pointer = 0
        w2_pointer = 0
        while w1_pointer <= (len(word1)-1) or w2_pointer <= (len(word2)-1):
            
            # global w1_pointer, w2_pointer
            if w2_pointer > (len(word2)-1) or w1_pointer > (len(word1)-1) :
                break
            newWord =  newWord+word1[w1_pointer]
            newWord = newWord+word2[w2_pointer]
            w1_pointer += 1
            
            w2_pointer += 1
        # if w1_pointer <= len(word1)-1:
        while w1_pointer <= len(word1)-1:
            # global w1_pointer
            newWord = newWord + word1[w1_pointer]
            w1_pointer += 1
            
        # else:
        while w2_pointer <= len(word2)-1:
            newWord = newWord + word2[w2_pointer]
            w2_pointer += 1
            
        return newWord
