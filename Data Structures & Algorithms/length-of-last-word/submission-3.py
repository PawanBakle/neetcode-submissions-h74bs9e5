class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = True
        last_len = []
        length = 0
        for i in range(len(s)):
            if s[i] != " ":
                flag = False
                length += 1
            elif s[i] == " ":
                flag = True
                last_len.append(length)
                length = 0
        last_len.append(length)
        for i in range(len(last_len)):
            if last_len[-1] == 0:
                last_len.pop()
            
            else:
                return last_len.pop()
