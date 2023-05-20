class Solution:
    #string t is longer, string s is sub 
    def isSubsequence(self, s: str, t: str) -> bool:
        currT = len(t)
        currS = len(s)
        
        if (s == ""):
            return True 
        while True: 
            if currT == 0 and currS == 0:
                return True
            if currS == 0:
                return True 
            elif currT == 0 and currS != 0:
                return False 
            elif (s[len(s) - currS] == t[len(t) - currT]):
                currT -= 1
                currS -= 1 
            else:
                currT -= 1
            
        