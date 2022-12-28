class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #-------------1--------------
        # dict = {}
        # for c in s:
        #     dict[c] = dict.get(c, 0) + 1
        
        # for c in t:
        #     if c in dict and dict[c] > 0:
        #         dict[c] -= 1
        #     else:
        #         return False
        
        # for c in dict:
        #     if dict[c] > 0:
        #         return False
                
        # return True

        #-------------2--------------
        return sorted(s) == sorted(t)
