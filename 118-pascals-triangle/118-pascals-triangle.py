class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      pascalTri = [] 
      for i in range(numRows): 
        # The first and last row elements are always 1.
        row = [None for x in range(i + 1)]
        row[0], row[-1] = 1, 1
        
        for j in range (1, len(row)-1):
          row[j] = pascalTri[i - 1][j - 1] + pascalTri[i - 1][j]
        pascalTri.append(row)
      return pascalTri

    #DP Problem 
    #Base Case: start and end = 1 
    #Recurrence relation: curr = pre[i-1] + prev[i] 
    #Time complexity: O(numRows^2) 