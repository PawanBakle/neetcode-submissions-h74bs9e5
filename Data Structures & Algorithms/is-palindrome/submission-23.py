class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if s == " ":
        #     return True
        
        k = ''
        for i in s:
            if i.isalnum():
                k += i.lower()
            # else:
            #     continue
            # if i in (" ",'1','2','3','4','5','6','7','8','9','!',',',"",',',' ','?','%','#','(',')','*','@','!','`','^',"'",".",";",':'):
            #     continue
            # i = i.lower()
            # k = k + i
        left = 0
        right = len(k) - 1
        half = len(k) // 2
        # if half < 2:
        #     return False
        # if len(k) == 1:
        #     return True
        while left < half:
            if k[left] == k[right]:
                left += 1
                right -= 1
            else:
                return False
        return True