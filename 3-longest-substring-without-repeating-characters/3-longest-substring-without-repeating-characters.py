class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      # sliding window method  - AIM: without repeating characters
      currMax = 0 
      seenSoFar = []

      if len(s) == 0:
        return 0 
      if len(s) == 1:
        return 1
      for i in range (len(s)-1): 
        currMax = len(seenSoFar) if currMax < len(seenSoFar) else currMax 
        seenSoFar = []
        seenSoFar.append(s[i])
        for j in range (i+1, len(s)):
          if (s[j] not in seenSoFar):
            seenSoFar.append(s[j])
          else:
            currMax = len(seenSoFar) if currMax < len(seenSoFar) else currMax 
            seenSoFar = [] 
            break
          
      return len(seenSoFar) if currMax < len(seenSoFar) else currMax 
    
            