class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        strLen = len(s)
        
        seenS = {}
        seenT = {}
        currS = ""
        currT = "" 
        
        for i in range(len(s)): 
            if (s[i] in seenS):
                currS += seenS[s[i]]
            else:
                currS += str(i)
                seenS[s[i]] = str(i)

            if (t[i] in seenT):
                currT += seenT[t[i]]
            else:
                currT += str(i)
                seenT[t[i]] = str(i)  
            
            if (currS != currT):
                return False 
            
        return True 
                