class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if (rowIndex == 0):
            return [1]
        if (rowIndex == 1):
            return [1,1] 
        else: 
            arr = self.getRow(rowIndex -1)
            return [1,] + self.helper(arr) + [1,]
    
    def helper(self, array):
        result = [] 
        for i in range (len(array) - 1):
            result.append(array[i]+array[i+1])
        return result 
            
        