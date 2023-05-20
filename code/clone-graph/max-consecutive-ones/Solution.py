class Solution(object):
     
    def findMaxConsecutiveOnes(self, nums):
        maxOnes = 0
        """
        :type nums: List[int]
        :rtype: int
        """
        chain = 0
        for x in nums: 
            if (x == 1):
                chain+=1;
            if (x == 0):
                if (chain > maxOnes):
                    maxOnes = chain 
                chain = 0 

        return maxOnes  if (chain < maxOnes) else chain
            
        
