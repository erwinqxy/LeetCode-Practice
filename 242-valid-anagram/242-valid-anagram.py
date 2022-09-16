class Solution(object):
    def isAnagram(self, s, t):
      sortedS = sorted(s)
      sortedT = sorted(t)
      
      return sortedS == sortedT 