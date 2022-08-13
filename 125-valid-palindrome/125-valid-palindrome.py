class Solution:
    def isPalindrome(self, s: str) -> bool:
      
      p1 = 0 
      p2 = len(s) - 1
      while p1 < p2:
        c1 = s[p1].lower() 
        c2 = s[p2].lower()  
        if (c1.isalnum()):
          if (c2.isalnum()):
            if c1 == c2:
              p1 += 1
              p2 -= 1
            else: return False 
          else:
            p2 -= 1 
        else:
          p1 += 1 
      return True 