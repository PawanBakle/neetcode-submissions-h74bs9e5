class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # s.reverse()
        
        # two pointers approch
        left_side = 0
        right_side = len(s) -1
        while left_side < right_side:
        # for i in range(len(s)//2):
            s[left_side],s[right_side] = s[right_side],s[left_side] 
            left_side += 1 
            right_side -= 1 
        # 1 -> [t,e,e,n]0,3 -> 1,2 
        # 2 -> [t,e,e,n]1,2 half = 2 0,1 2,1

        # 3 -> [] 0,1,2



