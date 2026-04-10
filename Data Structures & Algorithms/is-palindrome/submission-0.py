import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join(s.split())

        #tabacat 
        #tabaact
        # k = ''.join(c for c in s if s.isalnum())
        k =  re.sub(r'[^a-zA-Z0-9]', '', s)
        k = k.lower()
        a = 0
        b = len(k)-1
        halfs = len(k)//2
        # if halfs % 2 != 0:
        #     halfs += 1
        '''
        half -> 3
        0,7 -> t(0<3),t  1,6 ->  a,a(1,3) 2,5 -> b,c(2<3)
        '''
        while a < halfs:
            if k[a] == k[b]:
                a += 1
                b -= 1
            else:
                return False
        return True




