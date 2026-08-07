class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
            s_split = s.split()
            # it's a list now
            pattern_dict = {}
            for key in pattern:
                if key not in pattern_dict:
                    pattern_dict[key] = 1
                else:
                    continue
            # pattern = {a:1, b:1}

            if len(s_split) != len(pattern):
                return False
            # [dog, cat, cat, dog]
            for i in range(len(s_split)):
                if s_split[i] not in pattern_dict.values():
                    for key in pattern_dict:
                        if pattern_dict[key] == 1:
                            pattern_dict[key] = s_split[i]
                            break
           # pattern = {a:dog, b:cat}
            
            for i in range(len(pattern)):
                if pattern_dict[pattern[i]] != s_split[i]:
                    return False
                
                # return False
        
            return True





