class Solution:
    def numberOfSteps(self, n: int) -> int:
      count = 0
      while (n > 0):
        if (n % 2 == 0):
          n = n // 2 
          count += 1 
        else:
          n -=1 
          count += 1
      return count 
    
    
# Time: O(log n) because n // 2 -> half the space 
# Space: O(1) -> constant 
# Question about conditions 