class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      substrings = {} 
      max_ = 0 
      n = len(s) 
      
      i = 0 
      for j in range(n): 
        if s[j] in substrings:
          i = max(substrings[s[j]], i)
          
        max_ = max(max_, j - i + 1)
        substrings[s[j]] = j + 1
        
      return max_