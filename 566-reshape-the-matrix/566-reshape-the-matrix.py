class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        #Check for the number of elements 
        noOfEle = len(mat) * len(mat[0])
        if noOfEle != (r*c):
          return mat
        
        newMat = []
        cCount = 0
        currRow = [] 
        for row in mat:
          for x in row: 
            if (cCount < c): 
              currRow.append(x)
              cCount += 1
            else: 
              newMat += [currRow,] 
              currRow = [] 
              currRow.append(x)
              cCount = 1
        newMat += [currRow,] 
        return newMat
            
          
          