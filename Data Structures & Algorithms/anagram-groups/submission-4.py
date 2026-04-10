class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c_ana = {}
        app_lis = {}
        for j in strs:
            sort_mac = ''.join(sorted(j))
            if app_lis.get(sort_mac,None) == None:
                app_lis[sort_mac] = []
                app_lis[sort_mac].append(j)
            else:
                
                app_lis[sort_mac].append(j)
            # for i in j:
            #     if c_ana.get(i,None) == None:
            #         c_ana[i] = 1
            #     else:
            #         c_ana[i] += 1
            # # sort_mac = sorted(c_ana)
            # sort_mac = ''.join(sorted(c_ana))
        
            # if app_lis.get(sort_mac,None) == None:
            #     app_lis[sort_mac] = []
            #     app_lis[sort_mac].append(j)
            # else:
                
            #     app_lis[sort_mac].append(j)
            # c_ana = {}
        return list(app_lis.values())
        # c_ana = {}
        # for i in strs:
        #     if c_ana.get(i,None) == None:
        #         c_ana[i] = 1:
        #     else:
        #         c_ana[i] += 1