class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sort = sorted(s)
        # t_sort = sorted(t)
        # if s_sort == t_sort:
        #     return True
        # return False
        s_st = {}
        t_st = {}
        # create a hashmap to store both arrays
        # and compare 'em
        for i in range(len(s)):
            val = s_st.get(s[i],None)
            if val == None:
                s_st[s[i]] = 1
            else:
                s_st[s[i]] += 1
        for i in range(len(t)):
            val = t_st.get(t[i],None)
            if val == None:
                t_st[t[i]] = 1
            else:
                t_st[t[i]] += 1


        sorted_dict = dict(sorted(s_st.items()))
        sorted_tdict = dict(sorted(t_st.items())) 
        if sorted_dict == sorted_tdict:
            return True
        return False
        