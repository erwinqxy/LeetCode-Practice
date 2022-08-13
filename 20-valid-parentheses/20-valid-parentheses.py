class Solution:
    def isValid(self, s: str) -> bool:
        pairings = {')':'(', '}':'{', ']':'['}
        opens = ['(', '{', '[']
        
        stack = "" 
        
        if len(s) <= 1:
          return False
        
        for i in range (len(s)):
          if (s[i]) in opens:
            stack += s[i]
          else: 
            if stack == "":
              return False 
            toPop = pairings[s[i]]
            topOfStack = stack[-1]
            if toPop != topOfStack:
              return False 
            else:
              stack = stack[:-1]
        return stack == "" 